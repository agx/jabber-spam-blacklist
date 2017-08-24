#! /usr/bin/python3
#
# (C) 2017 Guido Günther <agx@sigxcpu.org>
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import argparse
import yaml


def to_ejabberd_yaml(hosts):
    out = {'access_rules':
           {
            's2s': [{'deny': hosts}, 'allow'],
           }
    }
    return yaml.safe_dump(out, default_flow_style=False)


def to_ejabberd_erl(hosts):
    out = "%% -*- mode: erlang -*-\n"
    for host in hosts:
        out += '{{s2s_host, "%s"}, deny}.\n' % host
    return out
    

def main():
    parser = argparse.ArgumentParser(description='Convert XMPP spammer blacklist to server format.')
    parser.add_argument('--format', dest='format', choices=['ejabberd-erl', 'ejabberd-yaml'],
                        help='The output format', default='ejabberd-yaml')
    parser.add_argument('--out', type=str, default='-',
                        help='the output file tor produce')
    parser.add_argument('input', metavar='INPUT', type=str,
                        help='the input file to process')

    args = parser.parse_args()

    with open(args.input) as f:
        hosts = yaml.load(f)['spamhosts']

    if args.format == 'ejabberd-yaml':
        out = to_ejabberd_yaml(hosts)
    elif args.format == 'ejabberd-erl':
        out = to_ejabberd_erl(hosts)
    else:
        raise Exception("No support for format %s" % args.format)

    outfile = '/dev/stdout' if args.out == '-' else args.out
    with open(outfile, 'w') as f:
        f.write(out)

    return 0


if __name__ == '__main__':
    sys.exit(main())
