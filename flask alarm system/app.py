from flask import Flask, render_template, request

app = Flask(__name__)

def EIPGSMProgramming():
    print("Put IP/GSM Programming Here")
def ZoneProgramming(ZoneList):
    a = int(input('''
Enter Zone Number:'''))
    if a == 00:
        return
    while a != 00:
        b = int(input(f'''
{a} Enter Zone Type:'''))
        if b == 00:
            break
        c = input(f'''
{a} Enter Partition Num: ''')
        if c == "*":
            c = 1
        else:
            pass
        print("Report codes are split into 0-9, A-F enter those digits.")
        d = input(f'''
{a} Report Code 1st:''')
        e = input(f'''
{a} Report Code 2nd:''')
        d = d + e
        e = int(input(f'''
0 = EOL
1 = NC
2 = NO
3 = Zone Doubling
4 = Double-Balanced
{a} Enter Hardware Type:'''))
        f = int(input(f'''
0 = 10mSec
1 = 350mSec
2 = 700mSec
3 = 1.2 seconds
{a} Enter Response Type:'''))
        g = int(input(f'''
2 = AW (Aux Wired Zone)
3 = RF (Supervised RF Transmitter)
4 = UR (Unsupervised RF Transmitter)
5 = Button Type RF Transmitter (Unsupervised)
    {a} Enter Input Type:'''))
        ZoneList.update({a: [b, c, d, e, f, g]})
        print(f'''
ZN  ZT  P   RC   HW:RT
    {a}    {b}  {c}   {d}   {e}:{f}
    ''')
        a = a + 1
def FunctionKeyProgramming():
    print("Put Function Key Programming")
def ExpertMode():
    print("Put Expert Mode")
def OutputDeviceMapping():
    print("Put Output Device Mapping")
def OutputProgramming():
    print("Put Output Programming")
def ZoneListProgramming():
    print("Put Zone List Programming Here")
def AlphaProgramming():
    print("Put Alpha Programming")
def Update_Data_Feilds(kinput, y):
    x = input(f'''{kinput} Enter data:''')
    y.update({kinput: x})
    print("Data field updated")
    print(data_feilds)
def InstallerMode(user_codes, data_feilds, zone_list):
    while True:
        print("Installer Code 20")
        kinput = input().split("*")
        kinput = int(kinput[1])
        if kinput == 20:
            while True:
                new_installer_code = input("Enter New Installer Code: ")
                new_installer_code_verification = input("Re-Enter New Installer Code: ")
                if new_installer_code == new_installer_code_verification:
                    user_codes.update({"Installer": new_installer_code})
                    break
                else:
                    print("Please make Installer code match")
        if 21 <= kinput <= 28:
            Update_Data_Feilds(kinput, data_feilds)
        if kinput == 29:
            EIPGSMProgramming()
        if 30 <= kinput <= 55:
            Update_Data_Feilds(kinput, data_feilds)
        if kinput == 56:
            ZoneProgramming(zone_list)
            print(zone_list)
        if kinput == 57:
            FunctionKeyProgramming()
        if kinput == 58:
            ExpertMode()
        if 59 <= kinput <= 78:
            Update_Data_Feilds(kinput, data_feilds)
        if kinput == 79:
            OutputDeviceMapping()
        if kinput == 80:
            OutputProgramming()
        if kinput == 81:
            ZoneListProgramming()
        if kinput == 82:
            AlphaProgramming()
        if 83 <= kinput <= 96:
            Update_Data_Feilds(kinput, data_feilds)
        if kinput == 97:
            user_codes.update({"Installer":'4112'})
            user_codes.update({"Master": '1234'})
            data_feilds.clear()
            zone_list.clear()
            print(data_feilds, zone_list, user_codes)
            return
        if kinput == 98:
            user_codes.update({"Installer": None})
            return
        if kinput == 99:
            return
        if 160<kinput<199:
            Update_Data_Feilds(kinput, data_feilds)
def Change_User_Code(user_codes, display):
    x = display.split("8")
    user = x[1]
    two_digit_user_code = int(user[0] + user[1])
    if two_digit_user_code == 1:
        print("You Can't change installer code like this")
    else:
        pass
    print(two_digit_user_code)
    new_code = user[2]+user[3]+user[4]+user[5]
    new_code_verification = user[6]+user[7]+user[8]+user[9]
    if new_code == new_code_verification:
        user_codes.update({two_digit_user_code: new_code})
        print("User Code Updated")
        return
    if new_code != new_code_verification:
        print("Make sure the codes match and enter them again")
def Show_Arm_Status(arm_status):
    if arm_status == False:
        print("***Disarmed Ready to Arm***")
    elif arm_status == True:
        print("***Armed Ready to Disarm***")
armed = False
data_feilds = {}
zone_list = {}
user_code = {
    1 :"4112",
    2 :"1234",
    3: "2116"
    }
while True:
    Show_Arm_Status(armed)
    display = input("Enter User Code: ")
    if user_code[1] == None:
        print('''Installer Locked Out of Programming
Execute the back door method''')
        input("Press Enter")
        user_code.update({1 : '4112'})
    if len(display) == 4:
        if display in user_code.values() and armed == False:
            armed = True
        else:
            armed = False
    else:
        pass
    if len(display) == 7:
        if (user_code[1] + "800") in display:
            InstallerMode(user_code, data_feilds, zone_list)
    if len(display) == 15:
        if (user_code[2] + '8') in display:
            Change_User_Code(user_code, display)
    if display == 'show user codes':
        print(user_code)

@app.route('/process_display', methods=['POST'])
def process_display():
    if request.method == 'POST':
        data = request.get_json()
        pressed_key = data.get('display')

        # Your logic to handle the pressed key goes here
        # Example: Check conditions and update variables accordingly

        response_data = {'status': 'success', 'message': 'Key pressed successfully'}
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)