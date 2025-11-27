visits_file = open('visit_log.csv', 'r')
funnel_file = open('funnel.csv', 'w')

funnel_file.write('user_id,source,category\n')

header = visits_file.readline()

for line in visits_file:
    data = line.strip().split(',')

    if len(data) >= 3:
        user_id = data[0]
        source = data[1]
        path = data[2]

        if 'category_' in path and '_checkout' in path:

            start_index = path.find('category_') + 9  # 9 - длина "category_"
            end_index = path.find('_checkout')

            category = path[start_index:end_index]
            funnel_file.write(f'{user_id},{source},{category}\n')

visits_file.close()
funnel_file.close()