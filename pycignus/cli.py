"""Console script for pycignus."""

import fire


def help():
    print("pycignus")
    print("=" * len("pycignus"))
    print(
        "PyCignus is an open-source, end-to-end information retrieval framework that allows users to easily build and deploy natural language search applications. It includes a Natural Language Search Engine (NLS) for indexing documents and searching them using natural queries."
    )


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
