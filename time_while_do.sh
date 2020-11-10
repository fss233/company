#!/bin/sh

source /etc/profile

#start_day=20191201
#end_day=20191231
start_day=20191001
end_day=20191130

dt=$start_day
while [[ $dt < `date -d "+1 day $end_day" +%Y%m%d` ]]
do
    #echo ${dt:0:4}/${dt:5-6}/${dt:7-8}
    #echo $dt
    exec_day=`date -d "$dt" +%Y/%m/%d/`
    echo $exec_day
    dir_rm="/backup_track/${exec_day}"
    echo "hadoop fs -rm -r $dir_rm"
    hadoop fs -rm -r $dir_rm
    hadoop jar /home/h_backup/bak_jar/bigdata-coldDataBak-1.0-SNAPSHOT-jar-with-dependencies-236-v1.jar com.zjxl.sjzt.mr.ColdDataBackup2InfluxDBMr /datasource/freight_track/${exec_day} /backup_track/${exec_day} > /home/h_backup/shell/log/${dt}_236.log


    ##dt++ 
    sleep 10
    dt=`date -d "+1 day $dt" +%Y%m%d`
done
