import vencrys_modules as vm

def main():
    dataobj = vm.Data("~/Vencrys/test/testdata.csv")
    print(dataobj.list_columns())

if __name__ == "__main__":
    main()
