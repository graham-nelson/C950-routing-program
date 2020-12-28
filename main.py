# Graham Nelson - Student ID: 000657218

import csv
import hashmap
import package
import distance_graph
import truck
import re


# O(n^2) - method is given a list of package objects, a graph, and a delivery truck.
# delivers all packages using the 'greedy' algorithm. method increments time, distance and
# visited nodes with each node that is visited.
def deliver_packages(packages, graph, delivery_truck):
    # repeats until all packages have been delivered
    while packages:
        # preselects first package for comparison
        package_to_deliver = packages[0]
        for p in packages:
            # checks all packages on the truck and finds the shortest path between current
            # location and package destination.
            if graph.get_distance(delivery_truck.node_index, p.node_index) < \
                    graph.get_distance(delivery_truck.node_index, package_to_deliver.node_index):
                package_to_deliver = p
        # distance traveled between current location and closest node
        distance_traveled = float(graph.get_distance(delivery_truck.node_index, package_to_deliver.node_index))
        # adds distance traveled to total truck miles
        delivery_truck.miles += distance_traveled
        # updates the location of the truck to the nearest node found above
        delivery_truck.node_index = package_to_deliver.node_index
        # updates the trucks time based on speed (18mph) and distance traveled
        delivery_truck.time += distance_traveled / delivery_truck.speed
        # updates the delivery time of the package with current time
        package_to_deliver.delivery_time = delivery_truck.time
        # updates package status
        package_to_deliver.status = 'Package Delivered'
        # removes delivered package from truck
        packages.remove(package_to_deliver)


# O(1) - returns the truck to the hub while updating the total miles the truck with the distance from the trucks current
# location to the hub.
def return_to_hub(delivery_truck, graph):
    hub = '4001 South 700 East'
    distance_traveled = float(graph.get_distance(delivery_truck.node_index, 1))
    delivery_truck.miles += distance_traveled
    delivery_truck.time += distance_traveled / delivery_truck.speed


# O(1) - takes in a time in minutes and returns a time formatted like "HH:MM AM/PM"
def format_minutes(t):
    time_hours = int(t / 60)
    time_minutes = t % 60
    if t < 720:
        am_pm = "AM"
        formatted_time = "%d:%02d" % (time_hours, time_minutes)
    else:
        am_pm = "PM"
        formatted_time = "%d:%02d" % (time_hours - 12, time_minutes)
    return formatted_time + ' ' + am_pm


# O(1) - takes a time in the format of "HH:MM AM/PM" and returns that time in minutes
def time_to_minutes(t):
    parsed = t.split(':')
    hours = parsed[0]
    parsed2 = parsed[1].split(' ')
    minutes = parsed2[0]
    am_pm = parsed2[1]

    time_in_minutes = float(hours) * 60 + float(minutes)
    if am_pm.upper() == 'AM':
        return time_in_minutes
    elif am_pm.upper() == 'PM':
        return time_in_minutes + 720


# O(1) - given a package and a time (in minutes), method returns the all package information and status at that time
# of day
def package_lookup(selected_package, selected_time):
    statement = '\nID: ' + str(selected_package.id) + ' Address: ' + str(selected_package.address) + \
                ' City: ' + str(selected_package.city) + ' Zip: ' + str(selected_package.zip) + \
                ' Delivery Deadline: ' + str(format_minutes(selected_package.delivery_deadline)) + \
                ' Weight: ' + str(selected_package.weight) + ' Status: '
    if selected_package is not None:
        if selected_time < selected_package.departure_time:

            statement1 = statement + 'At Hub'

            return statement1

        elif selected_package.delivery_time > selected_time > selected_package.departure_time:

            statement2 = statement + 'En Route'

            return statement2

        elif selected_time >= selected_package.delivery_time:
            statement3 = statement + selected_package.status + ' At ' + format_minutes(selected_package.delivery_time)

            return statement3


class Main:
    # creating hashmap for packages
    hm = hashmap.HashMap()
    g = distance_graph.Graph()

    # O(N) - importing csv package data
    with open('packages.csv') as csv_file:
        packages_csv = csv.reader(csv_file, delimiter=',')
        for row in packages_csv:
            id = int(row[0])
            node_index = int(row[1])
            address = row[2]
            city = row[3]
            state = row[4]
            zip = row[5]
            dl = int(row[6])
            weight = int(row[7])
            status = 'At The Hub'

            # creating package objects from csv file
            p = package.Package(id, node_index, address, city, state, zip, dl, weight, status)
            # adding package objects to hashmap
            hm.add(p.id, p)

    # O(N) - adding all vertices to adjacency matrix with data from csv file
    with open('distance_table.csv') as csv_file:
        distance_csv = csv.reader(csv_file, delimiter=',')
        for row in distance_csv:
            id = int(row[0])
            name = row[1]
            address = row[2]
            city = row[3]
            state = row[4]
            zip = row[5]

            # parsing csv to create vertex objects
            v = distance_graph.Vertex(id, name, address, city, state, zip)
            # adding vertex objects to the adjacency matrix
            g.add_vertex(v)

    # O(N^2) - adding all edges and weights to adjacency matrix
    with open('distance_table.csv') as csv_file:
        distance_csv = csv.reader(csv_file, delimiter=',')
        for row in distance_csv:
            vertex1_id = int(row[0])
            for i in range(6, 32):
                vertex2_id = i - 5
                edge_weight = row[i]
                g.add_edge(vertex1_id, vertex2_id, edge_weight)

    # O(N) - starting menu. enu will iterate through as many options as user specifies. Will only end when user
    # quits program or enters option #4
    while True:
        print("Welcome: ")
        print("\n 1. Run Program \n 2. Package Lookup \n 3. Print All Package Status \n 4. Exit \n")
        input1 = input('Please Select a Menu Option: ')

        # if user selects 'Run Program'
        if input1 == '1':
            # creating trucks
            truck1 = truck.Truck()
            truck2 = truck.Truck()

            truck1_departure_time = 480
            truck2_departure_time = 545

            # Average Case: O(1) Worst Case: O(N) for each retrieval - manually grouping packages
            packages1 = [
                hm.get(1), hm.get(2), hm.get(7), hm.get(8), hm.get(13), hm.get(14), hm.get(15), hm.get(16),
                hm.get(19), hm.get(20), hm.get(21), hm.get(29), hm.get(30), hm.get(33), hm.get(34), hm.get(39)
            ]

            packages2 = [
                hm.get(3), hm.get(4), hm.get(6), hm.get(10), hm.get(11), hm.get(12), hm.get(17), hm.get(18),
                hm.get(25), hm.get(26), hm.get(31), hm.get(32), hm.get(36), hm.get(37), hm.get(38), hm.get(40)
            ]

            packages3 = [
                hm.get(5), hm.get(9), hm.get(22), hm.get(23), hm.get(24), hm.get(27), hm.get(28), hm.get(35)
            ]

            # truck1 loading packages
            truck1.packages = packages1
            for p in truck1.packages:
                p.delivery_time = truck1_departure_time
                p.departure_time = truck1_departure_time
                p.status = 'En Route'
            # truck1 delivering packages
            truck1.time = truck1_departure_time
            deliver_packages(truck1.packages, g, truck1)

            # truck2 loading packages
            truck2.packages = packages2
            for p in truck2.packages:
                p.delivery_time = truck2_departure_time
                p.departure_time = truck2_departure_time
                p.status = 'En Route'
            # truck2 delivering packages starting at 9:05AM
            truck2.time = truck2_departure_time
            deliver_packages(truck2.packages, g, truck2)
            # truck1 returning to hub
            return_to_hub(truck1, g)
            # truck1 loading remaining packages
            # truck1 cannot leave until package #9 address is updated at 10:20AM
            truck1.time = 620
            truck1.packages = packages3
            for p in truck1.packages:
                p.time = truck1.time
                p.departure_time = truck1.time
                p.status = 'En Route'
            # truck1 delivering remaining packages
            deliver_packages(truck1.packages, g, truck1)

            print("\nAll Packages Delivered Successfully!\n")

            print('-----------------------------------------------------------------------\n')
            # printing total miles driven by both trucks
            print('Total Miles: ' + str(truck1.miles + truck2.miles))

        # if user selects 'Package Lookup'
        elif input1 == '2':
            while True:
                package_id = int(input("\nPlease Enter the ID (1-40) of the Package You Would Like To Find "
                                       "or Enter '0' to Exit: \n"))
                selected_package = hm.get(int(package_id))

                if package_id == 0:
                    print("\nExiting Lookup\n")
                    break

                elif selected_package is not None:
                    while True:
                        status_time = input("Please Enter Time You Would Like The Status At: "
                                            "(Example: 10:30 AM or 05:45 AM) \n")
                        format_check = re.match("[0-9][0-9]:[0-9][0-9] [A-Z][A-Z]", status_time)
                        if bool(format_check):
                            status_time = time_to_minutes(status_time)
                            print(package_lookup(selected_package, status_time))
                            break
                        else:
                            print("Please Enter Time In Correct Format (See Example)")

                else:
                    print('Please select a valid package ID...\n')

        # if user selects 'Print All Package Status'
        elif input1 == '3':
            status1 = 540
            status2 = 600
            status3 = 780
            print('\n-----------------------------------------------------------------------\n')
            print('All Package Status at ' + format_minutes(status1) + '\n')
            for i in range(1, 41):
                print(package_lookup(hm.get(i), status1))

            print('\n-----------------------------------------------------------------------\n')
            print('All Package Status at ' + format_minutes(status2) + '\n')
            for i in range(1, 41):
                print(package_lookup(hm.get(i), status2))

            print('\n-----------------------------------------------------------------------\n')
            print('All Package Status at ' + format_minutes(status3) + '\n')
            for i in range(1, 41):
                print(package_lookup(hm.get(i), status3))

        # if user selects 'Exit'
        elif input1 == '4':
            print('\nThank You, Have a Nice Day!\n')
            break

        # if user input does not match menu options
        else:
            print('\nPlease Select a Valid Menu Option...\n')
