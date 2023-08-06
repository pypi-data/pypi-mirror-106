#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import codecs
import os

import chardet

from TextGenerator import GenerateText, PrepareChain, __version__


def command_prepare(args):
    text = []
    for f in args.file:
        b = f.read()
        enc = chardet.detect(b)['encoding']
        t = b.decode('utf-8' if enc is None else enc).replace('\r', '')
        text.append(t)

    chain = PrepareChain.PrepareChain('\n'.join(text), args.out)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)


class TryLimitExceeded(Exception):
    pass


def _generate(generator, args):
    gen_txt = generator.generate(args.db)
    try_limit = args.try_limit
    if type(args.byte) is int:
        while len(gen_txt.encode('utf-8')) > args.length:
            if try_limit == 0:
                raise TryLimitExceeded
            gen_txt = generator.generate()
            try_limit -= 1

    return gen_txt


def command_generate(args):
    generator = GenerateText.GenerateText(args.sentence)
    for _ in range(args.time):
        print(_generate(generator, args))


def command_help(args):
    print(parser.parse_args([args.command, '--help']))


def check_positive(v):
    if int(v) <= 0:
        raise argparse.ArgumentTypeError(
            '%s is an invalid natural number' % int(v))
    return int(v)


def check_file(v):
    v = os.path.abspath(str(v))
    if not os.path.isfile(v):
        raise argparse.ArgumentTypeError(
            '%s is not file' % v)
    return codecs.open(v, 'rb')


def check_dbfile(v):
    v = os.path.abspath(str(v))
    if not os.path.isfile(v):
        raise argparse.ArgumentTypeError(
            '%s is not file' % v)
    return v


def parse_args(test=None):
    '''Parse arguments.'''
    global parser
    parser = argparse.ArgumentParser(
        prog='textgen',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='マルコフ連鎖を使った文章自動生成プログラム')

    subparsers = parser.add_subparsers()

    parser_prepare = subparsers.add_parser(
        'prepare', help='モデルをテキストから作成(chain.db)', aliases=['p'])
    parser_prepare.add_argument(
        'file', metavar='FILE', nargs='*', type=check_file,
        default=[open(0, 'rb')],
        help='テキストファイル (default: stdin)')
    parser_prepare.add_argument(
        '-o', '--out', metavar='DB', type=str,
        default='chain.db',
        help='出力DBファイル名 (default: %(default)s)')
    parser_prepare.set_defaults(handler=command_prepare)

    parser_generate = subparsers.add_parser(
        'generate', help='文章を生成する', aliases=['g'],
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser_generate.add_argument(
        '-s', '--sentence', metavar='NL', default=5,
        type=check_positive, help='生成する文数(>=0)')
    parser_generate.add_argument(
        '-b', '--byte', metavar='BYTE',
        default=None, type=check_positive,
        help='指定byte数以下の文生成を試行(>=0)')
    parser_generate.add_argument(
        '-n', '--time', metavar='TIME', default=1,
        type=check_positive, help='生成する回数(>=0)')
    parser_generate.add_argument(
        '-t', '--try_limit', metavar='LIMIT', default=100,
        type=check_positive, help='試行回数の上限(>=0)')
    parser_generate.add_argument(
        '-d', '--db', metavar='DB', type=check_dbfile,
        default='chain.db',
        help='チェインDBファイル')
    parser_generate.set_defaults(handler=command_generate)

    parser_help = subparsers.add_parser(
        'help', help='ヘルプを表示する', aliases=['h'])
    parser_help.add_argument(
        'command', help='ヘルプが表示されるコマンド名')
    parser_help.set_defaults(handler=command_help)

    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {}'.format(__version__))

    if test:
        return parser.parse_args(test)
    else:
        return parser.parse_args()


def main():
    args = parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
