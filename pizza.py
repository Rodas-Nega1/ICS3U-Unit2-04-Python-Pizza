#!/usr/bin/env python3

# Created by: Rodas
# Created on: Sep 2021
# This program calculates the cost of pizza


import constants


def main():

    # this function calculates the cost of pizza

    # input
    size = int(input("Enter the size of the pizza you want (inch): "))

    # process
    sub_total = (
        constants.LABOR + constants.RENT + (size * constants.COST_PER_INCH)
    )
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(size, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
