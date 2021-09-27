import csv

with open('/home/james/Desktop/CensusTrips/GEOLYTIX_OpenCensus_UK/CensusUK11Data.txt', 'r') as inpf:
    my_reader = csv.reader(inpf, delimiter='\t')
    with open('/home/james/Desktop/CensusTrips/GEOLYTIX_OpenCensus_UK/CensusUK11Data.csv', 'w') as outpf:
        my_writer = csv.writer(outpf, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        c = 1
        for r in my_reader:
            if c == 1:
                col_defs = []
                header = []
                for i in r:
                    if i == 'oacode':
                        col_type = 'varchar(9)'
                    else:
                        col_type = 'numeric'
                    col_defs.append(" ".join([i.lower(), col_type]))
                    header.append(i.lower())
                sql = 'CREATE TABLE geocrud.geolytix_census_2011({});\n'.format(','.join(col_defs))
                with open('/home/james/Desktop/CensusTrips/GEOLYTIX_OpenCensus_UK/create_table.sql', 'w') as outpf:
                    outpf.write(sql)
            else:
                out_record = []
                for i in range(0, len(header), 1):
                    inVal = r[i]
                    if i == 1:
                        outVal = inVal
                    else:
                        try:
                            outVal = int(inVal)
                        except ValueError:
                            outVal = float(inVal)
                    out_record.append(outVal)
                my_writer.writerow(out_record)
            c += 1

