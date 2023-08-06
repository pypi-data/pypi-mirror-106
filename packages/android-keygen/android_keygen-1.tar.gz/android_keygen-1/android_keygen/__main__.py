from android_keygen import keygen

#Get args
parser = keygen.make_parser()

args = vars(parser.parse_args())

#Check if we get args from exec file
do_exec = args["exec"]
exec_file = args["exec_file"]

#Run the program
if do_exec:
    import json
    all_args = json.load(open(exec_file,'r'))
    for args in all_args:
        keygen.main(args)
else:
    keygen.main(args)