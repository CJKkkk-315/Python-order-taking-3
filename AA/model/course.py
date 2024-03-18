import os
import json
from lib.helper import course_data_path,user_data_path,course_json_files_path,figure_save_path
import matplotlib.pyplot as plt
# d = os.path.dirname(__file__)
# parent_path = os.path.dirname(d)
# course_data_path = parent_path + "/data/course.txt"
# user_data_path = parent_path + "/data/user.txt"
# course_json_files_path = parent_path + "/data/source_course_files"
# figure_save_path = parent_path + "/static/img/"
class Course:

    def __init__(self,category_title="",subcategory_id=-1,subcategory_title="",subcategory_description="",
                 subcategory_url="",course_id=-1,course_title="",course_url="",num_of_subscribers=0,avg_rating=0.0,num_of_reviews=0):
        self.category_title = category_title
        self.subcategory_id = int(subcategory_id)
        self.subcategory_title = subcategory_title
        self.subcategory_description = subcategory_description
        self.subcategory_url = subcategory_url
        self.course_id = int(course_id)
        self.course_title = course_title
        self.course_url = course_url
        self.num_of_subscribers = int(num_of_subscribers)
        self.avg_rating = float(avg_rating)
        self.num_of_reviews = int(num_of_reviews)

    def __str__(self):
        return f"{self.category_title};;;{self.subcategory_id};;;{self.subcategory_title};;;{self.subcategory_description};;;{self.subcategory_url};;;{self.course_id};;;{self.category_title};;;{self.course_url};;;{self.num_of_subscribers};;;{self.avg_rating};;;{self.num_of_reviews}"

    def get_courses(self):
        res = []
        def SearchFiles(directory):
            fileList = []
            for root, subDirs, files in os.walk(directory):
                for fileName in files:
                    fileList.append(os.path.join(root, fileName))
            return fileList

        for dir in os.listdir(course_json_files_path):
            category = dir.split('_')[-1]
            directory = course_json_files_path + '\\' + dir
            fileList = SearchFiles(directory)
            for file in fileList:
                with open(file,'r') as f:
                    js = json.load(f)
                    subcategory_id = js['unitinfo']['source_objects'][0]['id']
                    subcategory_title = js['unitinfo']['source_objects'][0]['title']
                    subcategory_description = js['unitinfo']['source_objects'][0]['description']
                    subcategory_url = js['unitinfo']['source_objects'][0]['url']
                    for course in js['unitinfo']['items']:
                        course_id = course['id']
                        course_title = course['title']
                        course_url = course['url']
                        num_of_subscribers = course['num_subscribers']
                        avg_rating = course['avg_rating']
                        num_of_reviews = course['num_reviews']
                        res.append([category,subcategory_id,subcategory_title,subcategory_description,subcategory_url,course_id,course_title,course_url,num_of_subscribers,avg_rating,num_of_reviews])
        with open(course_data_path,'w',encoding='utf-8') as f:
            for i in res:
                f.write(';;;'.join(list(map(str,i)))+'\n')


    def clear_course_data(self):
        file = open(course_data_path, 'w').close()

    def generate_page_num_list(self, page, total_pages):
        if page <= 5:
            return list(range(1,min(10,total_pages+1)))
        elif page > 5 and page < total_pages - 4:
            return list(range(page-4,min(page+5,total_pages+1)))
        else:
            return list(range(total_pages-8,total_pages+1))

    def get_courses_by_page(self, page):
        res = []
        aw = []
        n = 0
        with open(course_data_path,'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            n += 1
            l = i.replace('\n','').split(';;;')
            aw.append(Course(*l))
            if len(aw) == 20:
                res.append(aw)
                aw = []
        if aw:
            res.append(aw)
        if not res:
            return (None,len(res),n)
        return (res[page-1],len(res),n)
    def delete_course_by_id(self, temp_course_id):
        flag = 0
        with open(course_data_path, 'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n', '').split(';;;')
            if int(l[5]) == temp_course_id:
                target = i
                flag = 1
        if flag:
            data.remove(target)
            with open(course_data_path, 'w',encoding='utf-8') as f:
                for i in data:
                    f.write(i)
            return True
        else:
            return False

    def get_course_by_course_id(self, temp_course_id):
        with open(course_data_path, 'r',encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            l = i.replace('\n', '').split(';;;')
            if int(l[5]) == temp_course_id:
                subscribers = int(l[8])
                rating = float(l[9])
                reviews = int(l[10])
                if subscribers > 100000 and rating > 4.5 and reviews > 10000:
                    comment = 'Top Course'
                elif subscribers > 50000 and rating > 4.0 and reviews > 5000:
                    comment = 'Popular Courses'
                elif subscribers > 10000 and rating > 3.5 and reviews > 1000:
                    comment = 'Good Courses'
                else:
                    comment = 'General Courses'
                return (Course(*l),comment)

    def get_course_by_instructor_id(self, instructor_id):
        res = []
        with open(user_data_path,'r',encoding='utf-8') as f:
            users = [i.replace('\n','').split(';;;') for i in f.readlines()]
        for user in users:
            if user[4] == 'instructor' and int(user[0]) == instructor_id:
                course_ids = user[-1].split('--')
        with open(course_data_path,'r',encoding='utf-8') as f:
            courses = [i.replace('\n','').split(';;;') for i in f.readlines()]
        for course in courses:
            if course[5] in course_ids:
                res.append(Course(*course))
        return (res[:20],len(res))

    def generate_course_figure1(self):
        plt.clf()
        with open(course_data_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        res = []
        d = {}
        for i in data:
            l = i.replace('\n', '').split(';;;')
            p = Course(*l)
            res.append(p)
        for i in res:
            if i.subcategory_title in d:
                d[i.subcategory_title] += int(i.num_of_subscribers)
            else:
                d[i.subcategory_title] = int(i.num_of_subscribers)
        res = [[i,j] for i,j in d.items()]
        res.sort(key=lambda x: x[1], reverse=True)
        x = [' '.join(i[0].split()[:3]) for i in res[:10]]
        y = [i[1] for i in res[:10]]
        plt.bar(x, y)
        plt.xticks(fontsize=7, rotation=20)
        plt.savefig(figure_save_path + 'course_figure1.png')
        return 'Hot Subcategory'

    def generate_course_figure2(self):
        plt.clf()
        with open(course_data_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        res = []
        d = []
        for i in data:
            l = i.replace('\n', '').split(';;;')
            p = Course(*l)
            res.append(p)
        for i in res:
            if i.num_of_reviews > 50000 :
                d.append([i.course_title,i.avg_rating])
        res = d[::]
        res.sort(key=lambda x: x[1])
        x = [' '.join(i[0].split()[:3]) for i in res[:10]]
        y = [i[1] for i in res[:10]]
        plt.bar(x, y)
        plt.xticks(fontsize=7, rotation=20)
        plt.savefig(figure_save_path + 'course_figure2.png')
        return 'Hot course bar'

    def generate_course_figure3(self):
        plt.clf()
        with open(course_data_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        res = []
        d = []
        for i in data:
            l = i.replace('\n', '').split(';;;')
            p = Course(*l)
            res.append(p)
        for i in res:
            if 100000 > i.num_of_subscribers > 10000:
                d.append([i.course_title, i.avg_rating])
        res = d[::]
        x = [' '.join(i[0].split()[:3]) for i in res[:10]]
        y = [i[1] for i in res[:10]]
        plt.scatter(x, y)
        plt.xticks(fontsize=7, rotation=20)
        plt.savefig(figure_save_path + 'course_figure3.png')
        return 'Popular courses scatter'

    def generate_course_figure4(self):
        plt.clf()
        with open(course_data_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        res = []
        d = {}
        for i in data:
            l = i.replace('\n', '').split(';;;')
            p = Course(*l)
            res.append(p)
        for i in res:
            if i.category_title in d:
                d[i.category_title] += 1
            else:
                d[i.category_title] = 1
        res = [[i,j] for i,j in d.items()]
        x = [' '.join(i[0].split()[:3]) for i in res[:10]]
        y = [i[1] for i in res[:10]]
        explode = [0, 0.3, 0, 0]
        plt.pie(x=y, labels=x,explode=explode)
        plt.xticks(fontsize=7, rotation=20)
        plt.savefig(figure_save_path + 'course_figure4.png')
        return 'Category proportion'

    def generate_course_figure5(self):
        plt.clf()
        with open(course_data_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        res = []
        have = 0
        nohave = 0
        for i in data:
            l = i.replace('\n', '').split(';;;')
            p = Course(*l)
            res.append(p)
        for i in res:
            if i.num_of_reviews != 0:
                have += 1
            else:
                nohave += 1
        x = ['Have reviews','Not have reviews']
        y = [have,nohave]
        plt.bar(x,y)
        for x, y in enumerate(y):
            plt.text(x, y + 100, '%s' % y, ha='center')
        plt.savefig(figure_save_path + 'course_figure5.png')
        return 'Is there any comment comparison'

    def generate_course_figure6(self):
        plt.clf()
        with open(course_data_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        res = []
        d = {}
        for i in data:
            l = i.replace('\n', '').split(';;;')
            p = Course(*l)
            res.append(p)
        for i in res:
            if i.subcategory_title in d:
                d[i.subcategory_title] += 1
            else:
                d[i.subcategory_title] = 1
        res = [[i, j] for i, j in d.items()]
        res.sort(key=lambda x: x[1])
        x = [' '.join(i[0].split()[:3]) for i in res[:10]]
        y = [i[1] for i in res[:10]]
        plt.bar(x, y)
        plt.xticks(fontsize=7, rotation=20)
        plt.savefig(figure_save_path + 'course_figure6.png')
        return 'Subcategory of minimum courses'
