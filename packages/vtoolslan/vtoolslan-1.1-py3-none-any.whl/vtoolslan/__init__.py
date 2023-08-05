"""vtoolslan
"""
from sys import argv
import os
import subprocess
from csv import DictWriter
from tabular_log import tabular_log
from json import loads, dumps
import requests
from programGUI import programGUI

__author__ = "help@castellanidavide.it"
__version__ = "01.01 2021-5-17"


class vtoolslan:
    def __init__(self,
                 verbose=False,
                 csv=False,
                 name=None,
                 add=False,
                 net=None,
                 type=None,
                 dbenable=False,
                 dburl=None,
                 dbtoken=None,
                 dbtable=None
                 ):
        """Where it all begins
        """
        self.setup(verbose, csv, dbenable, dburl, dbtoken,
                   dbtable, name, add, net, type)

        self.core()
        try:  # Try to run the core
            pass
        except BaseException:
            print("Error: make sure you have installed vbox on your PC")

    def setup(
        self, verbose, csv, dbenable, dburl, dbtoken, dbtable,
           name, add, net, type):
        """Setup
        """
        # Define main variabiles
        self.verbose = verbose
        self.csv = csv
        self.dbenable = dbenable
        self.dburl = dburl
        self.dbtoken = dbtoken
        self.dbtable = dbtable
        self.name = name
        self.add = add
        self.net = net
        self.type = type
        self.vboxmanage = 'C:\\Work\\VBoxManage' if os.name == 'nt' \
            else "vboxmanage"

        # Define log
        try:
            self.log = tabular_log(
                "C:/Program Files/vtoolslan/trace.log"
                if os.name == 'nt' else "~/trace.log", title="vtoolslan",
                verbose=self.verbose)
        except BaseException:
            self.log = tabular_log(
                "trace.log", title="vtoolslan", verbose=self.verbose)
        self.log.print("Created log")

        # Headers
        self.header = "VM_name,net,new"
        self.log.print("Headers inizialized")

        # Inizialize DB
        if self.dbenable:
            try:
                response = requests.request(
                    "POST", f"{self.dburl}",
                    headers={
                            'Content-Type': 'application/json',
                        'Authorization': f'''Basic {self.dbtoken}'''},
                    data=dumps({
                        "operation": "create_schema",
                        "schema": "dev"
                    })
                )
                self.log.print(f"By DB: {response.text}")
            except BaseException:
                self.log.print(f"Failed to create dev schema")

            for table, params in zip([self.dbtable],
                                     [self.header]):
                try:
                    response = requests.request(
                        "POST", f"{self.dburl}",
                        headers={
                                'Content-Type': 'application/json',
                            'Authorization': f'''Basic {self.dbtoken}'''},
                        data=dumps({
                            "operation": "create_table",
                            "schema": "dev",
                            "table": table,
                            "hash_attribute": "id"
                        })
                    )
                    self.log.print(f"By DB: {response.text}")
                except BaseException:
                    self.log.print(f"Failed to create {table} table")

                for param in params.split(","):
                    try:
                        response = requests.request(
                            "POST", f"{self.dburl}",
                            headers={
                                    'Content-Type': 'application/json',
                                'Authorization': f'''Basic {self.dbtoken}'''},
                            data=dumps({
                                "operation": "create_attribute",
                                "schema": "dev",
                                "table": table,
                                "attribute": param
                            })
                        )
                        self.log.print(f"By DB: {response.text}")
                    except BaseException:
                        self.log.print(
                            f"Failed to create {param} into {table} table")
            self.log.print("Inizialized DB")

        # If selected setup csv
        if self.csv:
            # Define files
            self.csvfile = "changes.csv"
            self.log.print("Defined CSV files' infos")

            # Create header if needed
            try:
                if open(self.csvfile, 'r+').readline() == "":
                    assert(False)
            except BaseException:
                open(self.csvfile, 'w+').write(self.header + "\n")

            self.log.print("Inizialized CSV files")

    def core(self):
        """Core of all project
        """

        self.get_output(["modifyvm", '"' + self.name + '"', f"--{self.net}", self.type])

        try:
            msg = {
                    "VM_name" : self.name,
                    "net" : self.net,
                    "new" : self.add
                }
            # If CSV enabled write into csv file
            if self.csv:
                DictWriter(
                    open(self.csv, 'a+', newline=''),
                    fieldnames=self.header.split(","),
                    restval='').writerow()

            # If DB enabled try to insert infos
            if self.dbenable:
                try:
                    response = requests.request(
                        "POST", f"{self.dburl}",
                        headers={
                                'Content-Type': 'application/json',
                                'Authorization': f'''Basic {self.dbtoken}'''
                        },
                        data=dumps({
                            "operation": "insert",
                            "schema": "dev",
                            "table": self.dbOStable,
                            "records": [
                                {

                                }
                            ]
                        })
                    )
                    self.log.print(f"By DB: {response.text}")
                except BaseException:
                    self.log.print(f"Failed the DB insert")
        except BaseException:
            self.log.print(f"Error taking data ...")

    def get_output(self, array):
        """ Gets the output by the shell
        """
        if os.name == 'nt':  # If OS == Windows
            cmd = self.vboxmanage
            for i in array:
                if " " in i:
                    i = "'" + i + "'"
                cmd += " " + i

            return vtoolslan.remove_b(subprocess.check_output(cmd, shell=False))
        else:
            return vtoolslan.remove_b(
                subprocess.Popen(
                    [self.vboxmanage] + array,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                ).communicate()[0])

    def remove_b(string):
        """Removes b'' by string
        """
        return str(string).replace("b'", "")[:-1:]


def laucher():
    """ Lauch all getting the params by the arguments passed on launch
    """
    # Get all arguments
    if "--help" in argv or "-h" in argv:
        print("To get an help to know how to use"
              "this program write into the shell:"
              "'man agentless', only for Linux.")
    elif "--batch" in argv or "-b" in argv:
        debug = "--debug" in argv or "-d" in argv
        csv = "--csv" in argv
        dbenable = dburl = dbtoken = dbOStable = dbNETtable = None

        for arg in argv:
            if "--url=" in arg:
                dburl = arg.replace("--url=", "")
            if "--token=" in arg:
                dbtoken = arg.replace("--token=", "")
            if "--table=" in arg:
                dbtable = arg.replace("--table=", "")

        # Launch the principal part of the code
        if dburl is not None and \
           dbtoken is not None and \
           dbtable is not None:
            vtoolslan(debug, csv, True, dburl, dbtoken, dbtable)
        else:
            vtoolslan(debug, csv)
    else:
        gui = programGUI(title="vtoolslan", instructions=[
            [
                {
                    "type": "text",
                    "title": "Insert VM name/id",
                    "id": "name"
                },
                {
                    "type": "bool",
                    "title": "Want you add net config?",
                    "id": "add"
                },
                {
                    "type": "text",
                    "title": "Insert the net you want to change (if not add)",
                    "id": "net"
                },
                {
                    "type": "list",
                    "title": "Insert new VM net type",
                    "options": 
                    [
                        "nat",
                        "natnetwork",
                        "bridged",
                        "internal"
                    ],
                    "id": "type"
                }
            ],
            [
                {
                    "type": "bool",
                    "title": "Want you to run it in the verbose mode?",
                    "id": "verbose"
                },
                {
                    "type": "bool",
                    "title": "Want you have a csv output?",
                    "id": "csv"
                }
            ],
            [
                {
                    "type": "text",
                    "title": "Insert url:",
                    "id": "url"
                },
                {
                    "type": "text",
                    "title": "Insert token:",
                    "id": "token"
                },
                {
                    "type": "text",
                    "title": "Insert table name:",
                    "id": "table"
                }
            ]
        ])

        if gui.get_values()["url"] is not None and \
                gui.get_values()["token"] is not None and \
                gui.get_values()["table"] is not None:
            vtoolslan(
                gui.get_values()["verbose"],
                gui.get_values()["csv"],
                gui.get_values()["name"],
                gui.get_values()["add"],
                gui.get_values()["net"],
                gui.get_values()["type"],
                True,
                gui.get_values()["url"],
                gui.get_values()["token"],
                gui.get_values()["table"]
            )
        else:
            vtoolslan(
                gui.get_values()["verbose"],
                gui.get_values()["csv"],
                gui.get_values()["name"],
                gui.get_values()["add"],
                gui.get_values()["net"],
                gui.get_values()["type"]
            )


if __name__ == "__main__":
    laucher()
