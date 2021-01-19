import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib as hl
import datetime as dt
import time
from colorama import Fore, Style

#=================variable=============================================================================================================================

index = 0
block = []
Previous_Hash = []
block_hash = [] #hash of block
data = []

#=================function=============================================================================================================================

def showdata():
    cleanlabel()
    temp = ''
    count = 0
    for i in data:
        keep = i.split('|')
        temp += "Block # " + str(count) + "\nAddress: " + keep[6] + "\n"
        if(count+1 != index):
            temp += " |\nV\n"
        count+=1
    output_label.configure(text=temp)
    print("\nBlock[] :", block)
    print("\nPrevious[] :", Previous_Hash)
    print("\nhash[] :", block_hash)
    print("\ndata[] :", data)

def hashfunction(num):
    x=str(num)
# นำข้อมูลที่ได้เข้า hash(sha256)
    hashing = hl.sha256(x.encode()).hexdigest()
    print("Hashing.....")
    time.sleep(0.2)
    if (hashing != " "):
        print("HashComplete!!!\n.")
        return hashing
    else :
        print("HashFailed!!!!!!!!!\n.")
        return None

def createblock():
    cleanlabel()
    insert = []
    global index
    if((name_entry.get() != "") and (from_team.get() != "") and (to_team.get() != "") and (price_entry.get() != "") and (price_entry.get()).isdigit()):
        print("Create ........")
        time.sleep(0.5)
# data[]
# Get address_block
        address = hl.md5(str(index).encode()).hexdigest()
# data_input = block#x | name | old_team | new_team | price | timestamp | address
        data_input = 'Block#' + str(index) + '|' +str(name_entry.get()) +'|'+ str(from_team.get()) +'|'+ str(to_team.get()) +'|'+ str(price_entry.get()) +'|'+ str(dt.datetime.now()) + '|' + str(address)
# data[] << data_input        
        data.append(data_input)
        hashing = hashfunction(data_input)
# block_hash << Hash(data_input)
        block_hash.append(hashing)
        show_hash = "Hash : " + block_hash[index]
        print(data[index].split("|"))
        print(show_hash)
        if (index == 0):
            pre=[]
            null_block = ''
# Previous_hash[]
# block#0 >> previous_block = 0x64
            for null_pre in range(64):
                null_block += '0'
            set_previous = null_block
            pre.append('Previous_Block#' + str(index))
            pre.append(set_previous)
            Previous_Hash.append(pre)
        elif (index != 0):
            pre =[]
            pre.append('Previous_Block#' + str(index))
            pre.append(block_hash[index-1])
            Previous_Hash.append(pre)
# block[]
# block[] = Block#x , address , Previous_Hash , block_hash
        if (hashing != " "):
            name_block = 'Block#' + str(index)
            insert.append(name_block)
            insert.append(address)
            insert.append(Previous_Hash[index][1])
            insert.append(block_hash[index])
            block.append(insert)
            print(block[index])
            print("Create Success\n")
#             messagebox.showinfo("Create Complete",block[index])
            #output_label.configure(text=hashing)
            index+=1
        else:
            print("Create Failed\n")
#             messagebox.showerror("Create Failed","Create Failed!!!!")
    else :
        print("Can't Create Input Invalid")
#         messagebox.showerror("Create Failed","Create Input Invalid!!!!")
    clear()
    
def statusblock():
    cleanlabel()
    global index
    if(index == 0):
        output_label.configure(text="Block don't found!!!!")
    elif(index > 0):
        current_hash = []
        pre_hash = []
        for i in block:
            current_hash.append(i[3])
            pre_hash.append(i[2])
        num = 0
        blockdraw = ''
        blockterminal = ''
        while(num != index):                
            if (num+1 < index):      
                if(current_hash[num] == pre_hash[num+1]):
                    blockterminal += '| Block #'+ str(num) + ' |'
                elif(current_hash[num] != pre_hash[num+1]):
                    red = Fore.RED + '| Block #'+ str(num) + ' |'
                    red_reset = Style.RESET_ALL
                    blockterminal += red + red_reset
            elif (num+1 == index):
                blockterminal += '| Block #'+ str(num) + ' |'
            blockdraw += '| Block #'+ str(num) + ' |'
            num+=1
            if(num != index):
                blockdraw += '<--'
        output_label.configure(text=blockdraw)
        print(blockterminal)
            
def searchblock():
    cleanlabel()
    search_show =''
    if(search_entry.get().isdigit()):
        if(int(search_entry.get()) <= index-1):
            block_search = ''
            block_search += 'Block#' + str(search_entry.get())
            num = 0
            for i in block:
                if block_search in i:
                    search_num = num
# เก็บ address ของ Block ที่ Search                    
                    search_address = i[1] 
                num+=1
            print("search_num: ", search_num , " " , search_address)
            for i in data:
                if search_address in i:
                    search_select = i.split('|')
                    search_show += "Block # " + str(search_num) + " : \nName: " + search_select[1] + "\nOld Team: " + search_select[2] + "\nNew Team: " + search_select[3] + "\nPrice: " + search_select[4] + "\nAddress: " + search_select[6] + "\nPrevious_Hash :\n" + str(Previous_Hash[search_num][1]) + "\nHash :\n" + str(block_hash[search_num]) + "\nTimestamp : " + search_select[5] + "\n\n"
            print(search_show)
            output_label.configure(text=search_show)
        else:
            print("Out Of range!!!!")            
    else:
        print("error search!!!!!")
    clear()
        
def checkblock():
    cleanlabel()
    check_show =''
    if(check_entry.get().isdigit()):
        if(int(check_entry.get()) < index-1):
            block_check = ''
            block_next = ''
            block_check += 'Block#' + str(check_entry.get())
            b_next = int(check_entry.get())+1
            block_next += 'Previous_Block#' + str(b_next)
            num = 0
# Get Previous_hash[]
            for j in Previous_Hash:
                print("\n",j,"\n")
                if block_next in j:
                    next_hash = j[1] #เก็บ hash ของ Block ถัดไป
                    print("next_hash: " ,next_hash)
# Get Current_hash & address
            for i in block:
                if block_check in i:
                    check_num = num
                    check_hash = i[3] #เก็บ hash ของ Block ที่ check
                    check_address = i[1] #เก็บ address ของ Block ที่ check
                    print("check_hash: ", check_hash, "check_address: ", check_address)
                num+=1
# check current & previous
# นำ address มาหาข้อมูลใน data
            if(check_hash == next_hash):
                for i in data:
                    if check_address in i:
                        check_select = i.split('|')
                        check_show += "Block # " + str(check_num) + " : \nName: " + check_select[1] + "\nOld Team: " + check_select[2] + "\nNew Team: " + check_select[3] + "\nPrice: " + check_select[4] + "\nAddress: " + check_select[6] + "\nPrevious_Hash :\n" + str(Previous_Hash[check_num][1]) + "\nHash :\n" + str(block_hash[check_num]) + "\nTimestamp : " + check_select[5] + "\n\n"
                        check_show += "/////////////////!!!!!!!!!!This Block is verify!!!!!!!////////////\n\n"
                output_label.configure(text=check_show)
            elif(check_hash != next_hash):
                for i in data:
                    if check_address in i:
                        check_select = i.split('|')
                        check_show += "Block # " + str(check_num) + " : \nName: " + check_select[1] + "\nOld Team: " + check_select[2] + "\nNew Team: " + check_select[3] + "\nPrice: " + check_select[4] + "\nAddress: " + check_select[6] + "\nPrevious_Hash :\n" + str(Previous_Hash[check_num][1]) + "\nHash :\n" + str(block_hash[check_num]) + "\nTimestamp : " + check_select[5] + "\n\n"
                        check_show += "/////////////////!!!!!!!!!!This Block is Unverify!!!!!!!////////////\n\n"
                output_label.configure(text=check_show)
                messagebox.showinfo('Info','This block has been changed!!!!')
        elif(int(check_entry.get()) == index-1):
            block_check = ''
            block_check += 'Block#' + str(check_entry.get())
            num = 0
            for i in block:
                if block_check in i:
                    check_num = num
# เก็บ address ของ Block ที่ check                    
                    check_address = i[1]
                num+=1
            print("check_current: ", check_num , " " , check_address)
            for i in data:
                if check_address in i:
                    check_select = i.split('|')
                    check_show += "Block # " + str(check_num) + " : \nName: " + check_select[1] + "\nOld Team: " + check_select[2] + "\nNew Team: " + check_select[3] + "\nPrice: " + check_select[4] + "\nAddress: " + check_select[6] + "\nPrevious_Hash :\n" + str(Previous_Hash[check_num][1]) + "\nHash :\n" + str(block_hash[check_num]) + "\nTimestamp : " + check_select[5] + "\n\n"
                    check_show += "////////////This CheckBlock is last of Block!!!!!!!!!!!!!//////////////\n\n"
            print(check_show)
            output_label.configure(text=check_show)
            
        else:
            print("Out Of range!!!!")            
    else:
        print("error check!!!!!")
    clear()
    
def editblock():
    cleanlabel()
    edit=''
    change_name1 = "prayut"
    change_name2 = "prawit"
    if edit_entry.get().isdigit():
        if(int(edit_entry.get()) <= index-1):
# message block ยีนยันการ edit
            if(int(edit_entry.get()) == index-1):
                if messagebox.askyesno('Change data Block','Are You Sure to change Last Block!!!!'):
                    edit_status = 1
                else:
                    edit_status = 0
            else:
                if messagebox.askyesno('Change data Block','Are You Sure to change this Block!!!!'):
                    edit_status = 1
                else:
                    edit_status = 0
            if(edit_status == 1):
                block_edit = ''
                block_edit += 'Block#' + str(edit_entry.get())
                num = 0
                for i in block:
                    if block_edit in i:
                        edit_num = num
# เก็บ address ของ Block ที่ edit
                        edit_address = i[1]
                    num+=1
                print("Block#", edit_num , " address: ", edit_address)
                for i in data:
                    if edit_address in i:
                        editor = i.split('|')
# เปลี่ยนชื่อของ block edit
                        if(editor[1] != change_name1):
                            editor[1] = change_name1
                        else:
                            editor[1] = change_name2
                    count_edit = 0
# นับ block edit
                for read in editor:
                    count_edit+=1
# นำข้อมูลใหม่ลง block edit
                for write in editor:
                    edit += write
                    if(count_edit != 1):
                        edit += '|'
                    count_edit-=1
                data[edit_num] = edit
                data_edit = data[edit_num]
                hashing_edit = hashfunction(data_edit)
                print("Hash Edit: ",hashing_edit)        
                print("data edit: ", data[edit_num])
                count_block = 0
                for j in block:
                    if edit_address in j:
                        print("find Address: ",j)
                        block[count_block][3] = hashing_edit
                    count_block+=1
                print("block after edit: ",block)
        else:
            print("Out Of range!!!!")
    else:
        print("error edit!!!!!!")
    
    clear()
    
def clear():
    name_entry.delete(0,"end")
    from_teambox.delete(0,"end")
    to_teambox.delete(0,"end")
    price_entry.delete(0,"end")
    search_entry.delete(0,"end")
    check_entry.delete(0,"end")
    edit_entry.delete(0,"end")
    
def cleanlabel():
    output_label.configure(text=" ")

#==================Configure=======================================================================================================================

app = tk.Tk()
app.title("BlockChain ตลาดซื้อขายนักบอล")
#app.minsize(width=700, height=500)
app.columnconfigure([0,2],minsize=100)
app.columnconfigure([1,3,6],minsize=1)
app.columnconfigure([4],minsize=200)
app.rowconfigure([0,1,2,3,4,5,6,7,8], minsize=20)

#showdata
app.columnconfigure([5], minsize=300)

#==================Component====================================================================================================================

status_button = tk.Button(app, text="StatusBlock", command=statusblock)
create_button = tk.Button(app, text="Create", command=createblock)
#create_button.pack()

search_entry = tk.Entry(width="10")
#search_entry.pack()
a1 = tk.Label(app, text=">>") 
search_button = tk.Button(app, text="Search", command=searchblock)
#search_button.pack()

check_entry = tk.Entry(width="10")
#check_entry.pack()
a2 = tk.Label(app, text=">>")
check_button = tk.Button(app, text="Check", command=checkblock)
#check_button.pack()

edit_entry = tk.Entry(width="10")
#edit_entry.pack()
a3 = tk.Label(app, text=">>")
edit_button = tk.Button(app, text="Edit", command=editblock)
#edit_button.pack()

show = tk.Button(app, text="show", command=showdata)
#--------------------------------------------------------------------------------------------------------------------------------

name_label = tk.Label(app, text="Name: ")
name_entry = tk.StringVar()
name_entry = ttk.Combobox(app, width=17, textvariable= name_entry)
name_entry['values'] = ('Lionel Messi',
                           'Mohamed Salah',
                           'Cristiano Ronaldo',
                          'Raheem Sterling',
                          'Roberto Firmino',
                          'David Silva',
                          'Neymar')

from_label = tk.Label(app, text="From: ")
from_team = tk.StringVar()
from_teambox = ttk.Combobox(app, width=17, textvariable= from_team)
from_teambox['values'] = ('Liverpool',
                           'Manchester United',
                           'Barcelona',
                          'Chelsea',
                          'NewCastle United',
                          'Arsenal',
                          'Manchester City')

to_label = tk.Label(app, text="To: ")
to_team = tk.StringVar()
to_teambox = ttk.Combobox(app, width=17, textvariable= to_team)
to_teambox['values'] = ('Liverpool',
                           'Manchester United',
                           'Barcelona',
                          'Chelsea',
                          'NewCastle United',
                          'Arsenal',
                          'Manchester City')

price_label = tk.Label(app, text="Price: $")
price_entry = tk.Entry()

#---------------------------------------------------------------------------------------------------------------------------------

output_label = tk.Label(app, justify='left')

#====================Position===================================================================================================================

status_button.grid(row=1, column=0)
create_button.grid(row=1, column=2)

search_entry.grid(row=3, column=0)
a1.grid(row=3, column=1)
search_button.grid(row=3, column=2)

check_entry.grid(row=5, column=0)
a2.grid(row=5, column=1)
check_button.grid(row=5, column=2)

edit_entry.grid(row=7, column=0)
a3.grid(row=7, column=1)
edit_button.grid(row=7, column=2)

show.grid(row=8,column=0)
#------------------------------------------------------------------------------------------------------------------------------------------

name_label.grid(row=1, column=3)
name_entry.grid(row=1, column=4)

from_label.grid(row=3, column=3)
from_teambox.grid(row=3, column=4)
to_label.grid(row=5, column=3)
to_teambox.grid(row=5, column=4)

price_label.grid(row=7, column=3)
price_entry.grid(row=7, column=4)

#-------------------------------------------------------------------------------------------------------------------------------------------------

output_label.grid(row=1, column=5, rowspan=7)

#====================================================================================================================================================

app.mainloop()
