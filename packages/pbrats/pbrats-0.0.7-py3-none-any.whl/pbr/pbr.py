#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io
import sys
import re
import pkgutil
import shutil
from bisect import bisect
#  pip install pandas openpyxl
import pandas as pd

from string import Template

# below codes copied from https://github.com/anntzer/redeal/blob/master/redeal/redeal.py with GPL-3.0 License
from enum import Enum

Strain = Enum("Strain", zip("CDHSN", range(5)))

class Contract:
    def __init__(self, level, strain, doubled=0, vul=False):
        if not (1 <= level <= 7 and hasattr(Strain, strain) and
                0 <= doubled <= 2):
            raise ValueError("Invalid contract")
        self.level = level
        self.strain = strain
        self.doubled = doubled
        self.vul = vul

    @classmethod
    def from_str(cls, s, vul=False):
        """
        Initialize with a string, e.g. "7NXX".  Vulnerability still a kwarg.
        """
        doubled = len(s) - len(s.rstrip("X"))
        return cls(int(s[0]), s[1], doubled=doubled, vul=vul)

    def score(self, tricks):
        """Score for a contract for a given number of tricks taken."""
        target = self.level + 6
        overtricks = tricks - target
        if overtricks >= 0:
            per_trick = 20 if self.strain in ["C", "D"] else 30
            base_score = per_trick * self.level
            bonus = 0
            if self.strain == "N":
                base_score += 10
            if self.doubled == 1:
                base_score *= 2
                bonus += 50
            if self.doubled == 2:
                base_score *= 4
                bonus += 100
            bonus += [300, 500][self.vul] if base_score >= 100 else 50
            if self.level == 6:
                bonus += [500, 750][self.vul]
            elif self.level == 7:
                bonus += [1000, 1500][self.vul]
            if not self.doubled:
                per_overtrick = per_trick
            else:
                per_overtrick = [100, 200][self.vul] * self.doubled
            overtricks_score = overtricks * per_overtrick
            return base_score + overtricks_score + bonus
        else:
            if not self.doubled:
                per_undertrick = [50, 100][self.vul]
                return overtricks * per_undertrick
            else:
                if overtricks == -1:
                    score = [-100, -200][self.vul]
                elif overtricks == -2:
                    score = [-300, -500][self.vul]
                else:
                    score = 300 * overtricks + [400, 100][self.vul]
            if self.doubled == 2:
                score *= 2
            return score

def matchpoints(my, other):
    """Return matchpoints scored (-1 to 1) given our and their result."""
    return (my > other) - (my < other)

def imps(my, other):
    """Return IMPs scored given our and their results."""
    imp_table = [
        15, 45, 85, 125, 165, 215, 265, 315, 365, 425, 495, 595, 745, 895,
        1095, 1295, 1495, 1745, 1995, 2245, 2495, 2995, 3495, 3995]
    return bisect(imp_table, abs(my - other)) * (1 if my > other else -1)

# Above codes copied from https://github.com/anntzer/redeal/blob/master/redeal/redeal.py with GPL-3.0 License

# for 1-16 boards
# https://tedmuller.us/Bridge/Esoterica/BoardVulnerability.htm
board_vul= "ONEBNEBOEBONBONE"
vul_table={"O": "None", "N": "N-S", "E": "E-W", "B": "Both"}
vul_maptable={"O": "", "N": "NS", "E":"EW", "B": "NSEW"}  # maptable to check based on declarer
# https://www.ebu.co.uk/laws-and-ethics/vp-scales
vp_scale_8boards=[  10.00,10.44,10.86,11.27,11.67,12.05,12.42,12.77,13.12,13.45,  # 0-9
                    13.78,14.09,14.39,14.68,14.96,15.23,15.50,15.75,16.00,16.23,
                    16.46,16.68,16.90,17.11,17.31,17.50,17.69,17.87,18.04,18.21,
                    18.37,18.53,18.68,18.83,18.97,19.11,19.24,19.37,19.50,19.62,
                    19.74,19.85,19.95,20.00 ]

# below are html template
id_template="""
    <td align='center'  class='td_nowrap td_leftSolid td_topSolid' >$declarer</td>
    <td align='center'  class='td_nowrap td_leftDotted td_topSolid' >$contract</td>
    <td align='center'  class='td_nowrap td_leftDotted td_topSolid' >$result</td>
    <td  colspan='2' align='right' class='td_nowrap td_leftSolid td_topSolid' ><font color='$scorecolor'>$score</font></td>
"""
onerow_template="""
<tr  bgcolor='#FAFAFA'>
    <td align='center' rowspan='2' class='td_top'><small>$boardno</small></td>
    <td align='center' rowspan='2' class='d_lt'><font color='#A0A080'>$vul</font></td>
    $host
    <td align='center' rowspan='2' class='d_lt'>$diff</td>
    <td align='center' rowspan='2' class='d_lt'>$hostimp</td>
    <td align='center' rowspan='2' class='d_lt'>$guestimp</td>
</tr>
<tr bgcolor="#F0F4F4">
    $guest
</tr>
"""

summary_template="""
<table class='TableFrame_blank1px' align='center' cellspacing='0px' cellpadding='6px'>
    <tr  bgcolor='#D5E0FF'>
        <td align='center'>主队 vs 客队</td>
        <td align='center'>IMP</td>
        <td align='center'>比赛胜利分</td>
    </tr>
    $teamsummary
</table>
"""
TOTAL_BOARDS=8 # later can be 12

def split_contract(contract):
    """
    split the handwriting quick notes into complete info
      S5Cxx+2 => 5CXX, S, +2, 13
      1. remove space
      2. change to uppercase
      3. auto append = if no +-=
      4  return tricks as well for each score later
    """
    upper=contract.upper().replace(" ", "")
    # check whether there is +-= result
    if not re.search(re.compile(r'\+|=|-'), upper):
        upper=upper+"="
    declarer = upper[0]

    # parse to get segments
    contract, sign, result = re.split("(\+|-|=)", upper[1:])
    if sign == "=":
        tricks = int(contract[0]) + 6 
    elif sign == "-":
        tricks = int(contract[0]) + 6 - int(result)
    else: # +
        tricks = int(contract[0]) + 6 + int(result)
    return declarer, contract, sign + result, tricks

def read_template(template_file):
    # read local first (debug), then module
    try:
        template = open(template_file, "r",encoding="utf-8").read()
        src = Template(template)
    except FileNotFoundError:
        if __name__ == "__main__":
            raise IOError("can't find file, debug?")
        else:
            template = pkgutil.get_data(__name__,template_file)
            src = Template(template.decode('utf-8'))
    return src

def read_teams(xls_file):
    # read raw data from xls, see sample student-group1.xlsx
    xl = pd.ExcelFile(xls_file)
    print("all sheets: ", xl.sheet_names)
    teams = []
    players = []
    if "team" not in xl.sheet_names:
        print("`team` sheet is needed inside excel")
    else:
        df = xl.parse("team")
        print("read teams from team sheet:")
        for index, row in df.iterrows():
            teams.append([row["host"],row["guest"]])
    for team in teams:
        a,b = team
        print("%s : %s" % (a,b))
        if a not in players:
            players.append(a)
        if b not in players:
            players.append(b)
    print("players:", players)
    return teams, players

def read_boards(xls_file, players):
    # read raw data from xls, see sample student-group1.xlsx
    df = pd.read_excel (xls_file).dropna(how="any")
    all_players = {}
    print("all boards: \n", df)
    for index, row in df.iterrows():
        # TODO, ugly
        if row["id"] == "url":
            print("url: ", row["id"])
        all_players[row["id"]] =  [ row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]

    boards = []
    for i in range(TOTAL_BOARDS):
        all_results = []
        for player in players:
            declarer, contract, result, tricks = split_contract(all_players[player][i])
            record = {"id": player, "declarer": declarer, "contract": contract, "result" : result, "tricks": tricks}
            all_results.append(record)
        boards.append(all_results)
    return boards

def html_suit(contract):
    suit_css = {
        'S':  "<font color=black>&spades;</font>",
        "H":  "<font color=red>&hearts;</font>",
        "D":  "<font color=red>&diams;</font>",
        "C":  "<font color=black>&clubs;</font>"
    }
    for k,v in suit_css.items():
        contract = contract.replace(k, v)
    return contract

def get_dealside(board_no):
    # return EW/NS for scoring
    if (board_no%2) == 0:
        dealside="NS"
    else:
        dealside="EW"
    return dealside

# fill one id for each board
def process_oneid(board,vuls, dealside):
    src = Template(id_template)
    contract = board["contract"]
    declarer = board["declarer"]
    if declarer in vul_maptable[vuls]:
        vul=True
    else:
        vul=False
    score = Contract.from_str(contract, vul).score(board["tricks"])
    if declarer in "EW":
        score = -score
    # need vul 
    # print(score)
    if score > 0:
        scorecolor="red"
    else:
        scorecolor="green"
    all = { "contract": html_suit(contract), "result": board["result"],
            "declarer" : board["declarer"], "score": score, "scorecolor": scorecolor}
    return src.safe_substitute(all), score

def onerow(idx, board, team):
    # for one row for each board with host/guest id
    src = Template(onerow_template)
    host_id, guest_id = team
    # TODO
    host = [d for d in board if d['id'] == host_id][0]
    guest = [d for d in board if d['id'] == guest_id][0]
    # need IMP, VP
    vul = vul_table[board_vul[idx]]
    dealside = get_dealside(idx)
    host_html, host_score = process_oneid(host, board_vul[idx], dealside)
    guest_html, guest_score = process_oneid(guest, board_vul[idx], dealside)
    score_diff = host_score - guest_score
    imp = imps(host_score,guest_score)

    host_imp=guest_imp=""
    if imp > 0:
        host_imp=str(imp)
    elif imp <0:
        guest_imp=str(-imp)
    all = { "boardno": idx+1, "vul": vul, "host": host_html, "guest" : guest_html, "diff" : score_diff, "hostimp": host_imp, "guestimp": guest_imp }
    return src.safe_substitute(all), host_imp, guest_imp

def get_match(boards, teamno, team):
    """
    calculate one match
    """
    rows = ""
    total_hostimp = 0
    total_guestimp = 0
    for idx, board in enumerate(boards):
        row,host_imp,guest_imp = onerow(idx, board, team)
        rows += row
        total_hostimp += int(host_imp) if host_imp else 0
        total_guestimp+= int(guest_imp) if guest_imp else 0

    # calculate VP from IMPs, it depends on board number
    diff_imp = total_hostimp - total_guestimp
    if abs(diff_imp) > len(vp_scale_8boards)-1:
        vp = vp_scale_8boards[-1] # 20.00
    else:
        vp = vp_scale_8boards[abs(diff_imp)]
    if diff_imp > 0:
        host_vp=vp
        guest_vp=20-vp
    else:
        guest_vp=vp
        host_vp=20-vp

    result = {
        "rows" : rows,
        "teamno": teamno,
        "teamhost" : team[0],
        "teamguest" : team[1],
        "hostimp" : total_hostimp,
        "guestimp": total_guestimp,
        "hostvp": format(host_vp,".2f"),
        "guestvp": format(guest_vp,".2f")
    }
    src = read_template("match-temp.html")
    contents = src.safe_substitute(result)
    return contents,(total_hostimp,total_guestimp), (host_vp,guest_vp)

def get_team_summary(summary):
    teams_html = ""
    print("team summary:")
    print("==============")
    for idx, team in enumerate(summary):
        teams, imp, vp = team
        print("%d, %s vs %s, %d : %d, %.2f : %.2f" % \
            (idx+1, teams[0], teams[1],imp[0],imp[1],vp[0],vp[1]))
        html =  "<tr><td><a href='#match-%d'>%s vs %s</a></td><td>%2d : %2d</td><td>%.2f : %.2f</td></tr>" %  \
            (idx+1, teams[0], teams[1],imp[0],imp[1],vp[0],vp[1])
        teams_html += html
    
    src = Template(summary_template)
    result={ "teamsummary" :teams_html } 
    contents = src.safe_substitute(result)
    return contents

def pbr(record_xls):
    """
    read xls file and generate related html
    """
    base_file = record_xls[:-len("xlsx")]
    output = base_file + "html"
 
    teams,players = read_teams(record_xls)
    boards = read_boards(record_xls, players)

    teams_html =""
    summary=[]
    for idx, team in enumerate(teams):
        html, imp, vp = get_match(boards, idx+1, team)
        teams_html += html
        summary.append([team,imp, vp])
    summary_html=get_team_summary(summary)
    result = { "teams" : teams_html, "summary" : summary_html}
    src = read_template("index-temp.html")
    contents = src.safe_substitute(result)

    with io.open(output, "w", encoding="utf-8") as text_file:
        print("write to file %s" % output)
        text_file.write(contents)

def usage():
    usage = """
    $ pbr sample # download sample xlsx
    $ pbr <record.xlsx> # check result
    see more for README
    """
    print(usage)

def download_sample():
    if __name__ == '__main__':
        print("dear contributor, do this in package mode")
        return
    sample_files=['student-group1.xlsx']
    for sample_file in sample_files:
        if os.path.exists(sample_file):
            print("%s already exists, ingore (or remove it first)" % sample_file)
        else:
            print("download sample file -> [%s]" % sample_file)
            shutil.copy(os.path.join(os.path.dirname(os.path.realpath(__file__)),sample_file),".")

def main():
    # print(sys.argv)
    if len(sys.argv) > 1:
        params = sys.argv[1:]
        if params[0] == "sample":
            download_sample()
        elif params[0] == "help":
            usage()
        else:
            record_xls=params[0]
            if record_xls.endswith(".xlsx"):
                pbr(record_xls)
            else:
                usage()
    else:
        usage()

if __name__ == '__main__':
    main()

