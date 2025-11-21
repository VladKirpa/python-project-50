from gendiff.cli import parser_cli


def main():
    parser = parser_cli()
    args = parser.parse_args()
    print(args)



if __name__ == '__main__':
    main()


