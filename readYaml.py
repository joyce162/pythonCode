import yaml


def get_testcase_from_yaml(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            testcase = yaml.safe_load(f)
            return testcase
    except Exception as e:
        print(e)

if __name__ == '__main__':
    testcase = get_testcase_from_yaml('loginTestcae.yml')
    print(type(testcase))

    case = testcase[0]
    print(case)
    url = case['baseInfo']['url']
    print(url)
    method = case['baseInfo']['method']
    print(method)
    header = case['baseInfo']['header']
    print(header)
    data = case['testcase'][0]['data']
    print(data)
