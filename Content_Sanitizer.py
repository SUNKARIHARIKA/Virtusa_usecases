'''
Core Python: The "SocialMedia" Content Sanitizer
Business Case: A startup is launching a safe social media platform for schools. They need a tool
that automatically "screens" posts for banned words and links before they go live. Problem Statement
Build a Content Moderator Script that scans a list of posts, replaces "Banned Words" with asterisks
(***), and extracts all web links for security clicking. Student Tasks:
1. List Processing: Start with a list of strings (Sample Posts). 
2. Word Masking: Use a banned_words = ["bad", "toxic", "hate"] list. 
If a post contains these, replace them using .replace(). 
3. Link Extraction: Use string slicing or the .startswith('http') method to find all URLs in the
posts and save them to a links_found.txt file. 4. Summary Dictionary: Create a dictionary that tracks 
how many times each user flagged the
"Moderator" (e.g., {'User123': 3, 'User456': 0}). 5. User Report: Print a final report: "Total Posts Screened: X | Cleaned: Y | Blocked: Z." Deliverable: A Python script that demonstrates "Cleaning" a messy text file into a "Safe" version.
'''
BANNED_WORDS = ["bad", "toxic", "hate"]
INPUT_FILE = "input_posts.txt"
CLEANED_FILE = "cleaned_posts.txt"
LINKS_FILE = "links_found.txt"
def mask_banned_words(text):
    """
    Replace banned words with ***
    """
    words = text.split()
    result = []
    for word in words:
        clean_word = word.lower().strip(".,!?()[]{}:;")
        if clean_word in BANNED_WORDS:
            result.append("***")
        else:
            result.append(word)
    return " ".join(result)
def extract_links(text):
    """
    Extract URLs starting with http or https
    """
    words = text.split()
    links = []
    for word in words:
        if word.startswith("http://") or word.startswith("https://"):
            # Remove trailing punctuation
            clean_link = word.strip(".,!?()[]{}:;")
            links.append(clean_link)

    return links
def get_user(text):
    """
    Extract username from format:
    User123: message
    """
    if ":" in text:
        return text.split(":")[0].strip()
    return "Unknown"
# MAIN PROCESSING FUNCTION
def process_posts(posts):
    total_posts = len(posts)
    cleaned_count = 0
    blocked_count = 0
    moderator_flags = {}
    all_links = []
    cleaned_posts = []
    for original_post in posts:
        user = get_user(original_post)
        # Extract links
        links = extract_links(original_post)
        all_links.extend(links)
        # Count banned words (IMPORTANT FIX)
        words = original_post.split()
        flag_count = 0
        for word in words:
            clean_word = word.lower().strip(".,!?()[]{}:;")
            if clean_word in BANNED_WORDS:
                flag_count += 1
        # Update moderator dictionary
        if flag_count > 0:
            moderator_flags[user] = moderator_flags.get(user, 0) + flag_count
            blocked_count += 1
        else:
            cleaned_count += 1
        # Clean post
        cleaned_post = mask_banned_words(original_post)
        cleaned_posts.append(cleaned_post)
    return total_posts, cleaned_count, blocked_count, moderator_flags, all_links, cleaned_posts
# FILE OPERATIONS
def read_input_file():
    file = open(INPUT_FILE, "r", encoding="utf-8")
    posts = []
    for line in file:
        line = line.strip()
        if line != "":
            posts.append(line)
    file.close()
    return posts
def write_output_file(filename, data):
    file = open(filename, "w", encoding="utf-8")
    for item in data:
        file.write(item)
        file.write("\n")
    file.close()
# REPORT FUNCTION
def print_report(total, cleaned, blocked, moderator_flags):
    print("\n================ FINAL REPORT ================\n")
    print(f"Total Posts Screened: {total}")
    print(f"Cleaned Posts: {cleaned}")
    print(f"Blocked Posts: {blocked}\n")

    print("Moderator Flag Summary:")
    if len(moderator_flags) == 0:
        print("No flags recorded.")
    else:
        for user, count in moderator_flags.items():
            print(f"{user}: {count} flags")
# MAIN FUNCTION
def main():
    posts = read_input_file()
    total, cleaned, blocked, flags, links, cleaned_posts = process_posts(posts)
    write_output_file(CLEANED_FILE, cleaned_posts)
    write_output_file(LINKS_FILE, links)
    print_report(total, cleaned, blocked, flags)
    print("\nFiles generated successfully:")
    print("- cleaned_posts.txt")
    print("- links_found.txt")
# EXECUTION START
if __name__ == "__main__":
    main()

