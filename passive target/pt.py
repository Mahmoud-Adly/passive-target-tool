#!/usr/bin/env python
import optparse  # using to accept argument from shell


def banner():
    print(
        """
        Passive information gathering.
        PT : Passive Target

            ██████╗ ████████╗
            ██╔══██╗╚══██╔══╝
            ██████╔╝   ██║   
            ██╔═══╝    ██║   
            ██║        ██║   
            ╚═╝        ╚═╝   
    """
    )


def get_arguments():
    parser = optparse.OptionParser()  # object of option to add variable and help for usr
    parser.add_option("-t", "--target", dest="target", help="To specify the target to search for")
    (options, arguments) = parser.parse_args()  # add value  from option add
    if not options.target:
        parser.error("[-] please specify an target , use --help for info ")
    return options


def get_search(target):
    print("\n Result <" + target + "> \n")
    print("Website" + " " * 26 + " Url")
    print("-" * 8 + " " * 26 + "-" * 5)
    with open(r"../../passive target/lists/websiteLink.txt", 'r') as link:
        with open(r"../../passive target/lists/websiteName.txt", 'r') as name:
            count = 0
            while True:
                count += 1

                # Get next line from file
                lineName = name.readline()
                lineLink = link.readline()

                # if line is empty
                # end of file is reached
                if not lineLink:
                    break
                if not lineName:
                    break
                # print("{}".format(line.strip()))
                nameUrl = lineName.strip()
                url = lineLink.strip() + target
                print("[+] " + '{0:25} |   {1:100}'.format(nameUrl, url) + "\n" + "----" * 30)

        link.close()
        name.close()


def execute_program():
    # object of function to read input of user
    options = get_arguments()

    # print variable current mac before changed
    current_target = options.target
    print("[+] current target -> " + str(current_target))
    # argument to function pass
    get_search(current_target)


if __name__ == '__main__':
    banner()
    execute_program()
    print("Done.")
