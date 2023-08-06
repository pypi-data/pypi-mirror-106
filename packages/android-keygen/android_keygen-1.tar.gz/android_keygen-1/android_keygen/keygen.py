import random, string, argparse, os, subprocess

def make_parser():
    parse = argparse.ArgumentParser(description = "Keygen args")

    parse.add_argument("--exec", default = False, help = "If true, we get params from the exec.json file.")
    parse.add_argument("--exec_file", default = "./exec.json", help = "The path to the exec.json file.")
    parse.add_argument("--password_length", default = 20, help = "The length of the generated password.")
    parse.add_argument("--key_password_length", default = 20, help = "The length of the generated key password.")
    parse.add_argument("--key_password", default = "", 
        help = "The key password if null it will be the same as the generated password. You can also set the input as \{generate\} to generate one.")
    parse.add_argument("--base_name", default = "my_key", help = "The name of the keystore file.")
    parse.add_argument("--user_name", default = "Tester", help = "The first and last name for the keystore input request.")
    parse.add_argument("--org_name", default = "Test Org", help = "The organiziation name.")
    parse.add_argument("--org_name_unit", default = "Test Org", help = "The organiziation unit name.")
    parse.add_argument("--city", default = "Test City", help = "The orgs city or locality.")
    parse.add_argument("--state", default = "Test City", help = "The orgs state or province.")
    parse.add_argument("--country_code", default = "+1", help = "The two letter country code.")
    parse.add_argument("--alias", default = "", help = "The alias name. If left empty, we use the base name.")
    parse.add_argument("--output_path", default = "./output", help = "The directory used to create the file.")
    parse.add_argument("--alg", default = "RSA", help = "The algorithm used to generate the key.")
    parse.add_argument("--size", default = 2048, help = "The size of the generated key.")
    parse.add_argument("--validity",default = 10000, help = "Determines how long the key is valid for.")

    return parse 

def make_password(length):
    #Create password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    return ''.join([random.choice(all) for _ in range(length)])

def main(args):

    #Get args
    length = args["password_length"]
    base_name = args["base_name"]
    alias = args["alias"]
    #Set alias to base name if empty string
    if alias == "":
        alias = base_name
    output_path = args["output_path"]
    alg = args["alg"]
    size = args["size"]
    validity = args["validity"]
    user_name = args["user_name"]
    org = args["org_name"]
    org_unit = args["org_name_unit"]
    city = args["city"]
    state = args["state"]
    country_code = args["country_code"]
    kplength = args["key_password_length"]
    key_password = args["key_password"]

    #Create password
    password = make_password(length)

    #Create keypassword
    if key_password == "":
        key_password = password
    elif key_password == "\{generate\}":
        key_password = make_password(kplength)
    else:
        key_password = password

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    #Create key
    os.system(f"cd {output_path}")

    command = f"keytool -genkey -v -keystore {base_name}.keystore -alias {alias} -keyalg {alg} -keysize {size} -validity {validity}"
    command_input = [password, password, user_name, org_unit, org, city, state, country_code, 'y', key_password]

    subprocess.run(command, input="\n".join(command_input), text=True)

    #Copy the data just in case.
    helper = f"Password: {password}\n"
    helper += f"Length: {str(length)}\n"
    helper += f"Base Name: {base_name}\n"
    helper += f"Key Password Length: {str(kplength)}\n"
    helper += f"Key Password: {key_password}\n"
    helper += f"Alias: {alias}\n"
    helper += f"Output Path: {output_path}\n"
    helper += f"Alg: {alg}\n"
    helper += f"Size: {size}\n"
    helper += f"Validity: {validity}\n"
    helper += f"User Name: {user_name}\n"
    helper += f"Org: {org}\n"
    helper += f"Org Unit: {org_unit}\n"
    helper += f"City: {city}\n"
    helper += f"State: {state}\n"
    helper += f"Country Code: {country_code}"

    with open(f"{output_path}/{base_name}_password.txt","w") as f:
        f.writelines(helper)
