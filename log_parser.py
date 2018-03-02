import collections
import datetime
import re
import sys
import argparse


# See Readme.MD for usage 
# TODO: group user agents by day , count ratio of gets/posts per day per os

# read in lines and select date filed, convert to string format, and add values to dictionary.
# once values are in dictionary sort dictionary in descending order. print sorted dictionary values to screen

def get_daily_requests():
    daily_totals = collections.defaultdict(int)
    with open(sys.argv[2]) as infile:
        for line in infile:
            try:
                field = line.split()
                date = field[3].strip('')
                timestamp = datetime.datetime.strptime(date, '[%d/%b/%Y:%H:%M:%S').strftime('%d/%b/%Y')
                daily_totals[timestamp] += 1
                sorted_totals = sorted(daily_totals.items(), key=lambda (k, v): v, reverse=True)
            except ValueError:
                print('Bad date format found in the file.')
                pass
        for k, v in sorted_totals:
            print "Day: %s" % k + " " + "Total: %s " % v


# get top 3 user agents from the log file using similar method described above

def get_user_agents():
    agents_totals = collections.defaultdict(int)
    with open(sys.argv[2]) as infile:
        for line in infile:
            try:
                field = line.split()
                user_agent = field[11]
                agents_totals[user_agent] += 1
                sorted_agents = sorted(agents_totals.items(), key=lambda (k, v): v, reverse=True)
            except IndexError:
                print('Array out of bounds')
        for k, v in sorted_agents[:3]:
            print "User Agent: %s" % (k) + " " + "Count : %s" % (v)


# just scanning the lines with simplex regex to get counts of GET/POSTS then calculating ratio at the end


def get_ratio():
    a_list = []
    get_regex = re.compile(r'GET')
    post_regex = re.compile(r'POST')

    with open(sys.argv[2]) as infile:
        try:
            for line in infile:
                a_list.append(line.split())
                total_requests = range(0, len(a_list))
                get_count = 0
            for x in total_requests:
                if get_regex.search(a_list[x][5]):
                    get_count = get_count + 1
            post_count = 0
            for x in total_requests:
                if post_regex.search(a_list[x][5]):
                    post_count = post_count + 1

        except IOError:
            "Could not read logfile"

        ratio = float(get_count) / (post_count)

        print "The total get_count is %s  and the total post_count is %s" % (get_count, post_count)
        print "The ratio of gets to posts overall is %.2f" % round(ratio, 2)


# setting up some positional arguments and subcommands here that can be called from the command line

def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True, help="Enter a filename")
    subparser = parser.add_subparsers()

    parser_get_daily_requests = subparser.add_parser('get_daily_requests', help="Get total daily requests")
    parser_get_daily_requests.set_defaults(func=get_daily_requests)

    parser_get_user_agents = subparser.add_parser('get_user_agents', help="Get top 3 user agents")
    parser_get_user_agents.set_defaults(func=get_user_agents)

    parser_get_user_agents = subparser.add_parser('get_ratio', help="Get ratio of GETS/POSTS")
    parser_get_user_agents.set_defaults(func=get_ratio)

    if len(sys.argv) <= 2:
        sys.argv.append('--help')

    args = parser.parse_args()
    args.func()


if __name__ == "__main__":

    try:
        setup_args()

    except IOError:
        print ("You must specify a logfile")
        sys.exit(1)
