import northgravity_python_sdk.northgravity as gx
import logging; log=logging.getLogger('GX SDK')
import time
import pandas as pd
import io, os


print(os.environ.get('NG_API_ENDPOINT', 'https://api.g-x.co'))
print(os.environ.get('NG_STATUS_GROUP_NAME', ''))
print('-' * 110)

#-----------------#
print('** TESTING DATALAKE HANDLER **')

# DatalakeHandler
dh = gx.DatalakeHandler()
fid = '6fceae97-f692-46a0-ade8-a26bd8603855'
group = 'damien.beneschi@northgravity.com_home'

# search
print(dh.search_file(file_name='prepared_data.csv', file_type='SOURCE', group_name=group))
print(dh.search_file(file_name='Concord Copper.csv', file_type=None, group_name=group))
print(dh.search_file(file_name='prepared_data.csv', file_type='SOURCE', group_name=None))


print(dh.get_info_from_id(file_id=fid))

print(dh.download_by_id(file_id=fid, dest_file_name='test/test.csv', save=True))
print(dh.download_by_id(file_id=fid, dest_file_name='test/test.csv', save=False))

print(dh.download_by_name(file_name='prepared_data.csv', group_name=group,
                          file_type='SOURCE', dest_file_name='test/test.csv', save=True))
print(dh.download_by_name(file_name='prepared_data.csv', group_name=group,
                          file_type='SOURCE', dest_file_name='test/test.csv', save=False))

print(dh.upload_file(file='test/test.csv', group_name=group, file_upload_name='test_sdk.csv', file_type='SOURCE'))

iodf = io.BytesIO(pd.read_csv('test/test.csv').to_csv(index=False).encode())
print(dh.upload_file(file=iodf, group_name=group, file_upload_name='test_sdk.csv', file_type='SOURCE'))


#-----------------#
# Status Handler
print('-' * 110)
print('** TESTING STATUS HANDLER **')
sth = gx.StatusHandler()

sth.info('TEST SDK')
time.sleep(10)

sth.warn('TEST SDK')
time.sleep(10)

sth.error('TEST SDK')
time.sleep(10)
sth.info('TEST SDK')


#----------#
# TaskHandler
print('-' * 110)
print('** TESTING DATALAKE HANDLER **')
sh = gx.TaskHandler()

print(sh.read_task_parameter_value(arg_name='First Dataset'))

print(sh.download_from_input_parameter(arg_name='First Dataset', dest_file_name=None, save=False))
print(sh.download_from_input_parameter(arg_name='First Dataset', dest_file_name=None, save=True))
print(sh.download_from_input_parameter(arg_name='First Dataset', dest_file_name='test/test.csv', save=True))

print(sh.write_task_parameter_value(output_name='Output', value='test'))

print(sh.upload_to_output_parameter(output_name='First Dataset', file='test/test.csv', group_name=group, file_type='SOURCE'))
print(sh.upload_to_output_parameter(output_name='First Dataset', file=iodf, group_name=group, file_upload_name='TEST.csv', file_type='SOURCE'))

#----------#
# Time Series Handler
print('-' * 110)
print('** TESTING TIMESERIES HANDLER **')
ts = gx.Timeseries()

# First Query
symbols = {'Symbol': "CME_CL"}
columns = 'Contract'

ts.retrieve_data_as_csv(file_name='ts_test.csv',
                        symbols=symbols,
                        columns=columns,
                        group_name='travis.nadelhoffer@northgravity.com_home'
                        #start_date='2021-01-04',
                        #end_date='2021-02-05'
                        )

print(pd.read_csv('ts_test.csv').head())

# Second query
symbols = {'Code': "GX0000103", 'PdType':'Month', 'Period':'2020-11', 'TimeRef':'1630'}
columns = 'Close'

ts.retrieve_data_as_csv(file_name='ts_test2.csv',
                        symbols=symbols,
                        columns=columns,
                        group_name='travis.nadelhoffer@northgravity.com_home'
                        #start_date='2021-01-04',
                        #end_date='2021-02-05'
                        )

print(pd.read_csv('ts_test2.csv').head())

#------------
print('** TEST FINISHED WITH NO ERROR **')