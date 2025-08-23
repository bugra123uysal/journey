select * from journee;

select ülke , Bölge from journee;
select ülke , alan from journee;
select ülke , döviz_fiyatý from journee;
select ülke , Nüfus from journee;
select ülke , Baþkent from journee;
select ülke , Trafik_yönü from journee;
select Bölge , Trafik_yönü from journee;

select * from journee order by  Nüfus desc;
select * from journee order by Nüfus asc ;

select * from journee order by alan  desc;
select * from journee order by alan asc;

select * from journee  where Nüfus < 1000000;
select * from journee where  alan < 100000;
select * from journee where Bölge='Europe';
select * from journee where Bölge='Asia';
select * from journee where Bölge='Americas';

select * from journee where Para_birimi= 'USD'
select * from journee where Para_birimi='EUR';
select * from journee where bm=1;
select * from journee where Trafik_yönü='left'
select * from journee where Trafik_yönü='right'






