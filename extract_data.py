import argparse

from wbtools.db.dbmanager import WBDBManager


def main():
    parser = argparse.ArgumentParser(description="Extract gene interaction network from caltech curation db")
    parser.add_argument("-N", "--db-name", metavar="db_name", dest="db_name", type=str)
    parser.add_argument("-U", "--db-user", metavar="db_user", dest="db_user", type=str)
    parser.add_argument("-P", "--db-password", metavar="db_password", dest="db_password", type=str, default="")
    parser.add_argument("-H", "--db-host", metavar="db_host", dest="db_host", type=str)
    args = parser.parse_args()

    db_manager = WBDBManager(dbname=args.db_name, user=args.db_user, password=args.db_password, host=args.db_host)
    gene_int = db_manager.gene.get_weighted_gene_interactions()
    gene_names = db_manager.gene.get_all_gene_names()
    for gene1, gene2, weight in gene_int:
        for gene1_name in gene_names[gene1.lstrip("WBGene")]:
            for gene2_name in gene_names[gene2.lstrip("WBGene")]:
                print(gene1_name, gene2_name, weight)


if __name__ == '__main__':
    main()
