cd $1
Current=`pwd`
mysql_path=/home/mysql/store_data
DIR_TMP=/home/mysql
rm -rf $DIR_TMP
mkdir  $DIR_TMP
mkdir  $mysql_path
chmod 777 $DIR_TMP
chmod 777 $mysql_path

/opt/mysql/bin/mysqldump -uroot -p!QAZxdr5 --tab=$mysql_path --opt EASY7
rm -rf $mysql_path/TAB_LOG.sql
rm -rf $mysql_path/TAB_LOG.txt

cd $mysql_path
for i in `ls *.sql`
do
tab_name=`echo $i|awk -F. '{print $1}'`
rm -rf $mysql_path/$tab_name
rm -rf $mysql_path/$tab_name.txt
/opt/mysql/bin/mysqldump -uroot -p!QAZxdr5 --opt --triggers  EASY7 $tab_name>$tab_name.sql
done

cd $DIR_TMP
tar -czvf store_data.tar.tgz store_data

touch easy7_mysql_database_import.sh
cat >>easy7_mysql_database_import.sh <<MAYDAY
#/bin/bash
DIR_TMP=/home/mysql
mysql_path=/home/mysql/store_data
mkdir \$DIR_TMP
sed -n -e "1,/^exit 0$/!p" \$0 > \${DIR_TMP}/store_data.tar.tgz 2>/dev/null
cd \$DIR_TMP
tar -xzvf store_data.tar.tgz
rm -rf store_data.tar.tgz
cd store_data
ls | grep ".sql" > ../filename.txt

cat \$DIR_TMP/filename.txt| while read tab_name
do
/opt/mysql/bin/mysql -uroot -p!QAZxdr5 EASY7<\$mysql_path/\$tab_name
done

cd ..
rm -rf store_data
rm -rf filename.txt
rm -rf filedata.txt
cd ..
rm -rf mysql
exit 0
MAYDAY

chmod 777 easy7_mysql_database_import.sh

cd $Current
startdate=`date -d today +%Y_%m_%d_%H_%M_%S`
cat $DIR_TMP/easy7_mysql_database_import.sh $DIR_TMP/store_data.tar.tgz >/home/$(date +"%Y-%m-%d")_backup/easy7_mysql_database_backup_$startdate.bin
chmod 777 /home/$(date +"%Y-%m-%d")_backup/easy7_mysql_database_backup_$startdate.bin

rm -rf $mysql_path
rm -rf $DIR_TMP/store_data.tar.tgz
rm -rf $DIR_TMP/easy7_mysql_database_import.sh