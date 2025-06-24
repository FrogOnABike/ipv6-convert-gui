from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions import compress_ipv6

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.title("IPv6 Compressor")
        self.__frame = ttk.Frame(self.__root,padding ="3 3 12 12",width=width,height=height)
        self.__frame.grid(column=0, row=0,sticky=(N,W,S,E))
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)
        
        self.ip_add = StringVar()
        ip_add_entry = ttk.Entry(self.__frame, width=40,textvariable=self.ip_add)
        ip_add_entry.grid(column=2, row=1,sticky=(W,E))
        self.converted_add = StringVar()
        # self.converted_add.set("Compressed Address: ")
        
        
        ttk.Label(self.__frame, textvariable=self.converted_add).grid(column=2,row=2,sticky=(W,E))
        ttk.Button(self.__frame,text="Compress", command=self._compress_ipv6_callback).grid(column=3,row=3,sticky=W)
       
        ttk.Label(self.__frame,text="Full IPv6").grid(column=1,row=1,sticky=(W,E))
        ttk.Label(self.__frame, text="Compressed Address:").grid(column=1,row=2,sticky=E)
        
        for child in self.__frame.winfo_children():
            child.grid_configure(padx=5,pady=5)
        
        ip_add_entry.focus()
        self.__root.bind("<Return>",self._compress_ipv6_callback)
        # self.converted_add.set(compress_ipv6(str(self.ip_add)))
        
        self.__root.mainloop()

    def _compress_ipv6_callback(self, event=None): # event=None makes it compatible with both button command and bind
        """
        Callback function executed when the Compress button is clicked or Enter is pressed.
        Retrieves the input, calls the compression function, and displays the result.
        """
        full_address = self.ip_add.get() # Correctly get the string value from StringVar

        if not full_address.strip(): # Check for empty or whitespace-only input
            messagebox.showwarning("Input Error", "Please enter an IPv6 address.")
            self.converted_add.set("(Input Required)")
            return

        try:
            compressed_address = compress_ipv6(full_address) # Call the imported function
            self.converted_add.set(f"{compressed_address}")
        except ValueError as e: # Catch specific errors from your compress_ipv6 if it raises them
            messagebox.showerror("Validation Error", str(e))
            self.converted_add.set("(Error)")
        except Exception as e: # Catch any other unexpected errors
            messagebox.showerror("Compression Error", f"An unexpected error occurred: {e}")
            self.converted_add.set("(Error)")
