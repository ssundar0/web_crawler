import os


# crawling new websites creates new projects(folders)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating your project " + directory)
        os.makedirs(directory)


# Making Queue and Crawled files
def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url) # don't put empty data
    if not os.path.isfile(crawled):
        write_file(crawled, '')     # don't put anything in starting


# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# write data onto existing file
def append_data(path, data):
    with open(path, 'a') as file:
        file.write(data + "\n")


# delete data of the file
def delete_data(path):
    with open(path, 'w'):
        pass  # do nothing (over-writing same file with blank content.)


# File to Set
def file_to_set(file_name):
    results = set()
    with open(file_name, "rt") as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# set to File
def set_to_file(links, file):
    delete_data(file)
    for link in sorted(links):
        append_data(file, link)



























