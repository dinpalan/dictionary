#! /usr/bin/env python3
#SHEBANG

def dikupadictionary():
    #dictionary
    modules = {'network':'netmiko','port':'scapy','tcp':'socket'}
    

    print("Printing Dictionary");
    print(modules)

    modules.update({'youtube':'pytube'})
    print("Printing Dictionary after update");
    print(modules)

    print("Printing Dictionary after update");
    print(modules.get('network'))

    del modules['youtube']
    print("Printing Dictionary after deletion");
    print(modules) 

    print("Printing Key from Dictionary");
    print(modules.keys())

    print("Printing Values from Dictionary");
    print(modules.values())
    
    modules.pop('tcp')
    print("Printing Dictionary after pop");
    print(modules)



def main():
    try:
        
        dikupadictionary()
            
    except KeyboardInterrupt:
        
        print("Exiting because of program interpreted by user"); print("Thanks for using my application");
       


if __name__=='__main__':
       main() 
