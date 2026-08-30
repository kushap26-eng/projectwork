# File Operator

class JournalManager:

    '''
    Handles all the basic file for the journal, such as adding new data, reading and organising records,
    searching for specific text, and clearing the file when needed. It also safely handles the errors that may occur
    while working with th file.
    '''
    def __init__(self,filename = "journal.text"):

        '''
        Initializes the journal file.
        Attributes:
             filename(str): Name of the file used to store journal entries.
        Returns: None
        '''
        self.filename = filename

    def new_entry(self):

        '''
        Adds a new journal entry to the file.
        The user enters the journal text and timestamp.
        The new entry is added at the end of the file.
        '''
        try:
            print("Enter your journal entry: ")
            entry_text =input()

            print("Enter current timestamp (YYYY-MM-DD HH:MM:SS)")
            print("Timestamp: ",end="")
            timestamp = input()

            file = open(self.filename,"a")
            print("[" + timestamp + "]",file=file)
            print(entry_text,file=file) 
            print("",file=file) 

            print("Entry added successfully!")
        except PermissionError:
            print("Permission denied. Cannot write to the journal file.")
        except Exception as e:
            print("An unexpected error occured.")

    def veiw_entry(self):

        '''
        Display all journal entries saved in the file.
        If the file does not exist or empty, an appropriate error message is displayed.
        '''
        try:
            file = open(self.filename,"r")
            content = file.read()
            file.close()

            content = content.strip()

            if not content:
                print("No journal entries found. Start by adding a new entry!")
                return

            print("Your Journal Entries: ")
            print(content) 

        except FileNotFoundError:
            print("The Journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Permission denied. Cannot write to the journal file.")
        except Exception as e:
            print("An unexpected error occurred.")


    def search_entry(self):

        '''
        Searches the journal file for a specific keyword or date
        The search is case case-insensitive, so uppercase and lowercase letters are treated the same.
        '''
        try:
            file = open(self.filename,"r")
            content = file.read()
            file.close()

            print("Enter a keyword or date to search: ")
            keyword = input().strip()

            lines = content.splitlines()
            entries = []
            cureent_entries = []

            for line in lines:
                if line.strip():
                    cureent_entries.append(line)
                else:
                    if cureent_entries:
                        entry_str = cureent_entries[0]
                        for item in cureent_entries[1:]:
                            entry_str = entry_str + " " + item
                        entries.append(entry_str)
                        cureent_entries = []

            if cureent_entries:
                entry_str = cureent_entries[0]
                for item in cureent_entries[1:]:
                    entry_str = entry_str + " " + item
                entries.append(entry_str)

            matching_entries = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    matching_entries.append(entry)

            if matching_entries:
                print("Matching Entries: ")

                for entry in matching_entries:
                    print(entry)
            else:
                print("No Entries were found for the keyword: " + keyword +".")
        except FileNotFoundError:
            print("The Journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Permission denied. Cannot write to the journal file.")
        except Exception as e:
            print("An unexpected error occurred.")


    def delete_entries(self):

        '''
        Deletes all journal entries after asking for confirmation.
        If the user enters "yes" all data in journal file is removed.
        Otherwise the deletion is cancelled.
        '''
        try:
            try:
                test_file = open(self.filename,"r")
                test_file.close()
            except FileNotFoundError:
                print("No journal entries to delete.")
                return

            print("Are you sure you want to delete all entries? (yes/no):",end="")
            confirm = input().strip().lower()

            if confirm == "yes":
                file = open(self.filename,"w")
                file.close()
                print("All journal entries have been deleted sucessfully!")
            else:
                print("Deletion Canceled.")
        except PermissionError:
            print("Permission denied. System lock prevents file mdifications.")
        except Exception as e:
            print("An unexpected error occured.")


def main():

    '''
    Controls the main working of the Personal Journal Manager.
    Displays the menu and allows the user to choose different journal operations 
    untill they select the exit option.
    '''

    manager = JournalManager()

    print("Welcome to the Personal Journal Manager!")

    while True:
        print("1.Add a new Entry")
        print("2.View all Entries")
        print("3.Search for an Entry")
        print("4.Delete all Entries")
        print("5.Exit")

        print("Enter your choice:")

        choice = input()

        if choice == "1":
            manager.new_entry()

        elif choice == "2":
            manager.veiw_entry()

        elif choice == "3":
            manager.search_entry()

        elif choice == "4":
            manager.delete_entries()

        elif choice == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")

            print("------ Journal Manager Documentation ------")
            print(JournalManager.__doc__)

            print("------ New Entry Documentation ------")
            print(JournalManager.new_entry.__doc__)

            print("------ View all Entry Documentation ------")
            print(JournalManager.veiw_entry.__doc__)

            print("------ Search Entry Documentation ------")
            print(JournalManager.search_entry.__doc__)

            print("------ Delete all Entry Documentation ------")
            print(JournalManager.delete_entries.__doc__)
            break

        else:
            print("Invalid option.please select valid option from menu.")

if __name__ == "__main__":
    main()