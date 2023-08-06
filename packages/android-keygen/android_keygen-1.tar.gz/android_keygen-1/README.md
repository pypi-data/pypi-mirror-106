## Installation 
    pip install android_keygen
    or run setup.py install

## Intro
    This is a simple tool for creating an android distribution key for your app.
    There's a bug that forces the generated .keystore to be dropped in the root directory. 
    I'll try and fix that soon. 

## Usage
    android_keygen --base_name {MYNAME}
    This will create your keystore in the output directory.

## Optional Args

    --exec, default = False, help = If true, we get params from the exec.json file.

    --exec_file, default = ./exec.json, help = The path to the exec.json file.

    --key_password_length, default = 20, help = The length of the generated key password.

    --password_length, default = 20, help = The length of the generated password.

    --key_password, default = , help = The key password if null it will be the same as the generated password. You can also set the input as \{generate\} to generate one.

    --base_name, default = my_key, help = The name of the keystore file.

    --alias, default = , help = The alias name. If left empty, we use the base name.

    --output_path, default = ./output, help = The directory used to create the file.

    --alg, default = RSA, help = The algorithm used to generate the key.

    --size, default = 2048, help = The size of the generated key.

    --validity,default = 10000, help = Determines how long the key is valid for.

    --user_name, default = Tester, help = The first and last name for the keystore input request.

    --org_name, default = Test Org, help = The organiziation name.

    --org_name_unit, default = Test Org, help = The organiziation unit name.

    --city, default = Test City, help = The orgs city or locality.

    --state, default = Test City, help = The orgs state or province.

    --country_code, default = +1, help = The two letter country code.