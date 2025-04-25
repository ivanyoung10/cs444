import re

def parse_file(file_path):
    #Parse main text file into nested hashtable
    #Include coordinates for heuristic in another hashtable

    file = open(file_path, "r")
    text = file.read()

    no_va_text = re.sub("va-", "", text)
    no_parse_list = re.split("\n", no_va_text)

    parsed_list = []
    ret_list = []

    for i in no_parse_list:
       step = re.split("-->", i)
       parsed_list.append(step)

       #gets rid of duplicated first element and nested list
       no_double = parsed_list.pop(0)
       ret_list.append(no_double)

    #removes last empty element in list
    _ = ret_list.pop()

    coordinates = {}

    #put all coordinates with cities in hashtable
    for sublist in ret_list:
        lat_and_long = []
        split_text = re.split(" ", sublist[0], 1)
        city = split_text[0]
        if re.search("N", split_text[1]):
            cords = re.split("N", split_text[1])
            deg_min_sec_lat = re.split(" ", cords[0])
            degrees = deg_min_sec_lat[0]
            minutes = deg_min_sec_lat[1]
            seconds = deg_min_sec_lat[2]

            lat = int(degrees) + (int(minutes) / 60) + (int(seconds) / 3600)
            lat_and_long.append(lat)

            if re.search("E", split_text[1]):
                deg_min_sec_long = re.split(" ", cords[1])
                degrees = deg_min_sec_long[1]
                minutes = deg_min_sec_long[2]
                seconds = deg_min_sec_long[3]

                long = int(degrees) + (int(minutes) / 60) + (int(seconds) / 3600)
                lat_and_long.append(long)

            if re.search("W", split_text[1]):
                deg_min_sec_long = re.split(" ", cords[1])
                degrees = deg_min_sec_long[1]
                minutes = deg_min_sec_long[2]
                seconds = deg_min_sec_long[3]

                long = -(int(degrees) + (int(minutes) / 60) + (int(seconds) / 3600))
                lat_and_long.append(long)



        if re.search("S", split_text[1]):
            cords = re.split("S", split_text[1])
            deg_min_sec_lat = re.split(" ", cords[0])
            degrees = deg_min_sec_lat[0]
            minutes = deg_min_sec_lat[1]
            seconds = deg_min_sec_lat[2]

            lat = -(int(degrees) + (int(minutes) / 60) + (int(seconds) / 3600))
            lat_and_long.append(lat)

            if re.search("E", split_text[1]):
                deg_min_sec_long = re.split(" ", cords[1])
                degrees = deg_min_sec_long[1]
                minutes = deg_min_sec_long[2]
                seconds = deg_min_sec_long[3]

                long = int(degrees) + (int(minutes) / 60) + (int(seconds) / 3600)
                lat_and_long.append(long)

            if re.search("W", split_text[1]):
                deg_min_sec_long = re.split(" ", cords[1])
                degrees = deg_min_sec_long[1]
                minutes = deg_min_sec_long[2]
                seconds = deg_min_sec_long[3]

                long = -(int(degrees) + (int(minutes) / 60) + (int(seconds) / 3600))
                lat_and_long.append(long)


        coordinates[city] = lat_and_long


    map = {}
    for sublist in ret_list:
        #for city and distance value
        sub_hash = {}
        cities = []
        distances = []

        city_cord = re.split(" ", sublist[0], 1)
        city = city_cord[0]

        parse_sublist = re.sub("^ ", "", sublist[1])
        conn_cities_cords = re.split(" ", parse_sublist)

        counter = 0
        for i in conn_cities_cords:
            if counter % 2 == 1:
                counter += 1
                distances.append(i)
            else:
                counter += 1
                cities.append(i)

        for i in cities:
            sub_hash[i] = distances[cities.index(i)]

        map[city] = sub_hash

    return map, coordinates
