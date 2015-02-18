import csv

def test_emails(fn, ln, mn, fi, li, mi, domain):

    # simple
    e_fn = "{}@{}".format(fn, domain) # {fn}
    e_ln = "{}@{}".format(ln, domain)# {ln}
    
    # basics
    e_fnln = "{}{}@{}".format(fn, ln, domain) # {fn}{ln}
    e_fnln_dot = "{}.{}@{}".format(fn, ln, domain) # {fn}.{ln}
    e_filn = "{}{}@{}".format(fi, ln, domain) # {fi}{ln}
    e_filn_dot = "{}.{}@{}".format(fi, ln, domain) # {fi}.{ln}
    e_fnli = "{}{}@{}".format(fn, li, domain) # {fn}{li}
    e_fnli_dot = "{}.{}@{}".format(fn, li, domain) # {fn}.{li}
    e_fili = "{}{}@{}".format(fi, li, domain) # {fi}{li}
    e_fili_dot = "{}.{}@{}".format(fi, li, domain) # {fi}.{li}
        
    # backwards
    e_lnfn = "{}{}@{}".format(ln, fn, domain) # {ln}{fn}
    e_lnfn_dot = "{}.{}@{}".format(ln, fn, domain) # {ln}.{fn}
    e_lnfi = "{}{}@{}".format(ln, fi, domain) # {ln}{fi}
    e_lnfi_dot = "{}.{}@{}".format(ln, fi, domain) # {ln}.{fi}
    e_lifn = "{}{}@{}".format(li, fn, domain) # {li}{fn}
    e_lifn_dot = "{}.{}@{}".format(li, fn, domain) # {li}.{fn}
    e_lifi = "{}{}@{}".format(li, fi, domain) # {li}{fi}
    e_lifi_dot = "{}.{}@{}".format(li, fi, domain) # {li}.{fi}

    # using middle name
    e_fimiln = "{}{}{}@{}".format(fi, mi, ln, domain) # {fi}{mi}{ln}
    e_fimiln_dot = "{}{}.{}@{}".format(fi, mi, ln, domain) # {fi}{mi}.{ln}
    e_fnmiln = "{}{}{}@{}".format(fn, mi, ln, domain) # {fn}{mi}{ln}
    e_fnmiln_dot2 = "{}.{}.{}@{}".format(fn, mi, ln, domain) # {fn}.{mi}.{ln}
    e_fnmnln = "{}{}{}@{}".format(fn, mn, ln, domain) # {fn}{mn}{ln}
    e_mnmnln_dot2 = "{}.{}.{}@{}".format(fn, mn, ln, domain) # {fn}.{mn}.{ln}

    # dashes
    e_fnln_dash = "{}-{}@{}".format(fn, ln, domain) # {fn}-{ln}
    e_filn_dash = "{}-{}@{}".format(fi, ln, domain) # {fi}-{ln}
    e_fnli_dash = "{}-{}@{}".format(fn, li, domain) # {fn}-{li}
    e_fili_dash = "{}-{}@{}".format(fi, li, domain) # {fi}-{li}
    e_lnfn_dash = "{}-{}@{}".format(ln, fn, domain) # {ln}-{fn}
    e_lnfi_dash = "{}-{}@{}".format(ln, fi, domain) # {ln}-{fi}
    e_lifn_dash = "{}-{}@{}".format(li, fn, domain) # {li}-{fn}
    e_li_fi_dash = "{}-{}@{}".format(li, fi, domain) # {li}-{fi}
    e_fimiln_dash = "{}{}-{}@{}".format(fi, mi, ln, domain) # {fi}{mi}-{ln}
    e_fnmiln_dash2 = "{}-{}-{}@{}".format(fn, mi, ln, domain) # {fn}-{mi}-{ln}
    e_fnmiln_dash2 = "{}-{}-{}@{}".format(fn, mi, ln, domain) # {fn}-{mi}-{ln}

    # underscores
    e_fnln_under = "{}_{}@{}".format(fn, ln, domain) # {fn}_{ln}
    e_filn_under = "{}_{}@{}".format(fi, ln, domain) # {fi}_{ln}
    e_fnli_under = "{}_{}@{}".format(fn, li, domain) # {fn}_{li}
    e_fili_under = "{}_{}@{}".format(fi, li, domain) # {fi}_{li}
    e_lnfn_under = "{}_{}@{}".format(ln, fn, domain) # {ln}_{fn}
    e_lnfi_under = "{}_{}@{}".format(ln, fi, domain) # {ln}_{fi}
    e_lifn_under = "{}_{}@{}".format(li, fn, domain) # {li}_{fn}
    e_lifi_under = "{}_{}@{}".format(li, fi, domain) # {li}_{fi}
    e_fimiln_under = "{}{}_{}@{}".format(fi, mi, ln, domain) # {fi}{mi}_{ln}
    e_fnmiln_under = "{}_{}_{}@{}".format(fn, mi, ln, domain) # {fn}_{mi}_{ln}
    e_fnmnln_under = "{}_{}_{}@{}".format(fn, mn, ln, domain) # {fn}_{mn}_{ln}

    return e_fn + " " + e_ln + " " + e_fnln + " " + e_fnln_dot + " " + e_filn + " " + e_filn_dot + " " + e_fnli + " " + e_fnli_dot + " " + e_fili + " " + e_fili_dot + " " + e_lnfn + " " + e_lnfn_dot + " " + e_lnfi + " " + e_lnfi_dot + " " + e_lifn + " " + e_lifn_dot + " " + e_lifi + " " + e_lifi_dot + " " + e_fimiln + " " + e_fimiln_dot + " " + e_fnmiln + " " + e_fnmiln_dot2 + " " + e_fnmnln + " " + e_mnmnln_dot2 + " " + e_fnln_dash + " " + e_filn_dash + " " + e_fnli_dash + " " + e_fili_dash + " " + e_lnfn_dash + " " + e_lnfi_dash + " " + e_lifn_dash + " " + e_li_fi_dash + " " + e_fimiln_dash + " " + e_fnmiln_dash2 + " " + e_fnmiln_dash2 + " " + e_fnln_under + " " + e_filn_under + " " + e_fnli_under + " " + e_fili_under + " " + e_lnfn_under + " " + e_lnfi_under + " " + e_lifn_under + " " + e_lifi_under + " " + e_fimiln_under + " " + e_fnmiln_under + " " + e_fnmnln_under

def parse_row(row):
    """Parses csv frow in form of dictionary"""
    parsed_row = {'id':row['ID']}
    parsed_row['city'] = row["City"]
    parsed_row['fn'] = row["First_Name"]
    parsed_row['ln'] = row["Last_Name"]
    parsed_row['mn'] = row["Middle_Name"]
    parsed_row['email_tests'] = test_emails(row['First_Name'],row['Last_Name'],row['Middle_Name'],row['First_Initial'],row['Last_Initial'],row['Middle_Initial'],row['Email_Domain'])
    return parsed_row

if __name__ == '__main__':

    with open('lead_list.csv', 'rb') as emails_csv:

        new_csv = open('email_list.csv', 'wb')
        new_fieldnames = ['id', 'city', 'fn',
                          'ln', 'mn', 'email_tests']
        csv_reader = csv.DictReader(emails_csv)
        csv_writer = csv.DictWriter(new_csv, fieldnames=new_fieldnames)
        csv_writer.writeheader()
        for row in csv_reader:
            parsed_row = parse_row(row)
            csv_writer.writerow(parsed_row)
        new_csv.close()


