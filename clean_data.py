import pandas as pd

df = pd.read_csv("data/stats/denormalized_entries.csv", error_bad_lines=False, index_col=False, dtype='unicode')

# keep only carry-in and dump entries
df = df[df["entry_type"].isin(['C', 'D'])]


# example
def show_percentages_entry_typ(player):
    # percentages of carry-ins and dump ins from AUSTON.MATTHEWS
    nb_total = len(df[df['entry_by'] == player])
    percentage_carry = (len(df[ (df['entry_by'] == player) & (df['entry_type'] == "C") ])/nb_total)*100
    percentage_dump = (len(df[ (df['entry_by'] == player) & (df['entry_type'] == "D") ])/nb_total)*100
    
    print(" %s : %d entries. %.2f%% carry-in and %.2f%% dumps" % (player, nb_total, percentage_carry, percentage_dump))

nb_carry = len(df[df.entry_type == "C"])
nb_dump= len(df[df.entry_type == "D"])
nb_carry_g = len( df[ (df.entry_type == "C") & (df.goal_total == "1")])
nb_dump_g = len( df[ (df.entry_type == "D") & (df.goal_total == "1")])
print("%.4f of carry ins convert to goals" % ( (nb_carry_g/ nb_carry) * 100 ))
print("%.4f of dumps ins convert to goals" % ( (nb_dump_g/ nb_dump) * 100 ))
print(nb_dump)
