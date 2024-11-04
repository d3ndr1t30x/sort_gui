import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TextFileMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text File Merger")
        self.root.geometry("800x400")

        # Left panel for added files
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.left_text = tk.Text(self.left_frame, wrap=tk.WORD)
        self.left_text.pack(fill=tk.BOTH, expand=True)
        
        self.upload_button = tk.Button(self.left_frame, text="Upload Text Files", command=self.upload_files)
        self.upload_button.pack(pady=5)
        
        # Right panel for merged file output
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.right_text = tk.Text(self.right_frame, wrap=tk.WORD)
        self.right_text.pack(fill=tk.BOTH, expand=True)

        self.merge_button = tk.Button(self.right_frame, text="Merge and Sort Files", command=self.merge_files)
        self.merge_button.pack(pady=5)

        self.download_button = tk.Button(self.right_frame, text="Download Merged File", command=self.download_file)
        self.download_button.pack(pady=5)

        # To store the contents of the uploaded files
        self.file_contents = []

    def upload_files(self):
        # Open file dialog to select multiple .txt files
        file_paths = filedialog.askopenfilenames(title="Select Text Files", filetypes=[("Text files", "*.txt")])
        
        for file_path in file_paths:
            if file_path:  # Check if a file is selected
                with open(file_path, 'r') as f:
                    content = f.read()
                    self.file_contents.append(content)
                    # Show file content in left text window
                    self.left_text.insert(tk.END, f"--- {os.path.basename(file_path)} ---\n")
                    self.left_text.insert(tk.END, content + "\n\n")

    def merge_files(self):
        # Concatenate all file contents and remove duplicates
        merged_content = "\n".join(self.file_contents)
        unique_lines = sorted(set(merged_content.splitlines()))
        
        # Display sorted and unique lines in the right text window
        self.right_text.delete(1.0, tk.END)
        self.right_text.insert(tk.END, "\n".join(unique_lines))

    def download_file(self):
        # Save the merged output to a new file
        output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if output_path:
            with open(output_path, 'w') as f:
                f.write(self.right_text.get(1.0, tk.END))
            messagebox.showinfo("Success", f"Merged file saved as {output_path}")

# Initialize Tkinter
root = tk.Tk()
app = TextFileMergerApp(root)
root.mainloop()
