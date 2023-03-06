import sys
import BAC0

BAC0.log_level('silence')
bacnet = BAC0.lite()


def do_things(address,object_type,object_instance):
        try:
            read_vals = f'{address} {object_type} {object_instance} presentValue'
            read_result = bacnet.read(read_vals)
            if isinstance(read_result, str):
                pass
            else:
                read_result = round(read_result,2)
            print(read_result)
        except Exception as error:
            print("read error")


def main():
    # args from Javascript
    first = sys.argv[1]
    second = sys.argv[2]
    third = sys.argv[3]
    fourth = sys.argv[4]

    # get sensor data
    do_things(second, third, fourth)

    # all done    
    bacnet.disconnect()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bacnet app error")
        bacnet.disconnect()