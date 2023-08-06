#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import re
from sql_formatter.format_file import format_sql


class HiveToClickhouse(object):


    def int_to_string(self, int_data):
        if isinstance(int_data, int):
            return str(int_data)
        else:
            raise TypeError("need int type get {}".format(type(int_data)))

    def replace_old_pattern(self, pattern, repl, hive_sql):
        return re.sub(pattern = pattern, repl = repl, string = hive_sql)

    def __replace_in(self, hive_sql):
        """
        把in后面的条件转为string
        :param hive_sql:
        :return:
        """
        result = re.search('\s*in.*?(\(.*?\))',hive_sql)
        if result:
            parttern = result.group(1)
            repl = tuple(['{}'.format(i.strip('"')) for i in parttern.strip('(').strip(')').split(',')])
            clickhouse_sql = self.replace_old_pattern(parttern, str(repl).strip('(').strip(')'), hive_sql)
            return clickhouse_sql
        return hive_sql

    def __replace_get_json_object(self, hive_sql):
        """
        替换get_json_object 函数
        :param hive_sql:
        :return:
        """
        result = re.search("get_json_object\((.*?),(.*?)\)", hive_sql)
        if result:
            parttern = 'get_json_object\(.*?,.*?\)'
            args = result.group(1)
            parameter = re.sub('\$.','',result.group(2))
            repl = f"JSONExtractString({args},{parameter})"
            clickhouse_sql = self.replace_old_pattern(parttern, repl, hive_sql)
            return clickhouse_sql
        return hive_sql

    def __replace_on(self, hive_sql):
        """
        把on后面=号两边的条件转为string
        :param hive_sql:
        :return:
        """
        data1 = re.findall('[\t]*ON\s*(.*?=\s*.*)\n', hive_sql)
        for pattern in data1:
            condition = pattern.split('=')
            condition_left = condition[0]
            condition_right = condition[1].strip(';')
            new_left = f'toString({condition_left.strip()})'
            new_right = f'toString({condition_right.strip()})'
            repl = '='.join([new_left,new_right])
            hive_sql = self.replace_old_pattern(pattern.strip(), repl, hive_sql)
        return hive_sql

    def __replace_db(self, hive_sql):
        """
        替换库名
        :param hive_sql:
        :return:
        """
        sql = re.sub('iyourcar_dw\.', 'iyourcar_hive.', hive_sql)
        sql = re.sub('iyourcar_new\.', 'iyourcar_hive.', sql)
        sql = re.sub('iyourcar_recommendation\.', 'iyourcar_hive.', sql)
        sql = re.sub('iyourcar_user\.', 'iyourcar_hive.', sql)
        sql = re.sub('iyourcar\.', 'iyourcar_hive.', sql)
        return sql

    def __replace_condition(self, hive_sql):
        """
        把=号两边的条件全部转为string
        :param hive_sql:
        :return:
        """
        data = re.findall('(\\s*[\S]*\\s*=\\s*[\S]*)', hive_sql)
        for condition_str in data:
            try:
                pattern = condition_str.strip('(').strip(')')
                condition = condition_str.split('=')
                condition_left = condition[0].strip('(')
                condition_right = condition[1].strip(';').strip(')')
                if condition_left.strip() in ('!','>','<'):
                    continue
                new_left = f' toString({condition_left.strip()})'
                new_right = f'toString({condition_right.strip()}) '
                repl = '='.join([new_left,new_right])
                hive_sql = hive_sql.replace(pattern, repl)
            except:
                continue
        return hive_sql

    def __replace_split(self, hive_sql):
        """
        替换split函数
        :param hive_sql:
        :return:
        """
        old_str_list = re.findall('(split\(.*,\s*\'.*?\'\)\[.*?\])', hive_sql)
        for old_str in old_str_list:
            data = re.findall('split\((.*),\s*\'(.*?)\'\)\[(.*?)\]', old_str)[0]
            d1 = data[0]
            d2 = data[1]
            d3 = data[2]
            new_str = 'splitByString(\'{}\',{})[{}]'.format(d2,d1,int(d3))
            hive_sql = hive_sql.replace(old_str, new_str)
        old_str_list = re.findall('(split\(.*,\s*\'.*?\'\))', hive_sql)
        for old_str in old_str_list:
            data = re.findall('split\((.*),\s*\'(.*?)\'\)', old_str)[0]
            d1 = data[0]
            d2 = data[1]
            new_str = 'splitByString(\'{}\',{})'.format(d2, d1)
            hive_sql = hive_sql.replace(old_str, new_str)
        return hive_sql

    def __replace_substring(self, hive_sql):
        """
        替换substring函数
        :param hive_sql:
        :return:
        """
        old_str_list = re.findall('substring\(.*?,\s*\d*,\s*\d*\)', hive_sql)
        for old_str in old_str_list:
            data = re.search('substring\((.*?),\s*(\d*),\s*(\d*)\)', old_str)
            str = data.group(1)
            start_position = data.group(2)
            end_position = data.group(3)
            if int(start_position) ==0:
                new_str = 'subString({},{},{})'.format(str, int(start_position)+1, end_position)
                hive_sql = hive_sql.replace(old_str, new_str)
        old_str_list2 = re.findall('substr\(.*?,\s*\d*,\s*\d*\)', hive_sql)
        for old_str in old_str_list2:
            data = re.search('substr\((.*?),\s*(\d*),\s*(\d*)\)', old_str)
            str = data.group(1)
            start_position = data.group(2)
            end_position = data.group(3)
            if int(start_position) == 0:
                new_str = 'subString({},{},{})'.format(str, int(start_position) + 1, end_position)
                hive_sql = hive_sql.replace(old_str, new_str)
        hive_sql = hive_sql.replace('substring', 'subString')
        hive_sql = hive_sql.replace('substr', 'subString')
        return hive_sql

    def __replace_date_add(self, hive_sql):
        """
        替换date_add函数
        :param hive_sql:
        :return:
        """
        old_str_list = re.findall('date_add\(.*?,\s*\d*\)', hive_sql)
        for old_str in old_str_list:
            new_str = re.sub(' ','',old_str)
            hive_sql = hive_sql.replace(old_str, new_str)
        return hive_sql

    def __replace_datediff(self, hive_sql):
        """
        替换datediff函数
        :param hive_sql:
        :return:
        """
        old_str_list = re.findall('datediff\(.*?,\s*.*\)', hive_sql)
        for old_str in old_str_list:
            data = re.search('datediff\((.*?),\s*(.*)\)', old_str)
            start_date = data.group(1)
            end_date = data.group(2)
            new_str = 'dateDiff(\'day\',{},{})'.format(end_date, start_date)
            hive_sql = hive_sql.replace(old_str, new_str)
        return hive_sql

    def __replace_arithmetic_operator(self, hive_sql):
        """
        把data列表内的运算符两边的条件转为string
        :param hive_sql:
        :return:
        """
        data = ['!=','>=','<=','>','<']
        for i in data:
            old_str_list = re.findall('([\S]*\\s*{}\\s*[\S]*)'.format(i), hive_sql)
            for condition_str in old_str_list:
                try:
                    if condition_str.startswith('if('):
                        pattern = condition_str.strip('(').strip(')').strip('if(').strip(',')
                    else:
                        pattern = condition_str.strip('(').strip(')').strip(',')
                    condition = pattern.split(f'{i}')
                    condition_left = condition[0].strip('(')
                    condition_right = condition[1].strip(';').strip(')')
                    if condition_right.startswith('='):
                        continue
                    new_left = f' toString({condition_left.strip()})'
                    new_right = f"toString({condition_right.strip().strip(',')}) "
                    repl = f'{i}'.join([new_left, new_right])
                    hive_sql = hive_sql.replace(pattern, repl)
                except:
                    continue
        return hive_sql

    @classmethod
    def execute(cls, hive_sql):
        sql = format_sql(hive_sql)
        sql = cls().__replace_in(sql)
        sql = cls().__replace_get_json_object(sql)
        sql = cls().__replace_db(sql)
        sql = cls().__replace_split(sql)
        sql = cls().__replace_substring(sql)
        sql = cls().__replace_date_add(sql)
        sql = cls().__replace_datediff(sql)
        sql = cls().__replace_condition(sql)
        sql = cls().__replace_arithmetic_operator(sql)
        return sql











