select * from joucsv;

select ülke , Bölge from joucsv;
select ülke , alan from joucsv;
select ülke , döviz_fiyatý from joucsv;
select ülke , Nüfus from joucsv;
select ülke , Baþkent from joucsv;
select ülke , Trafik_yönü from joucsv;
select Bölge , Trafik_yönü from joucsv;
select ülke , nufus_yogunlu from joucsv ;

select ülke , kýþýbaþý_alan from joucsv;

select * from joucsv order by  Nüfus desc;
select * from joucsv order by Nüfus asc ;

select Bölge, ülke , nufus_yogunlu from joucsv order by nufus_yogunlu desc;
select Bölge ,ülke , nufus_yogunlu from joucsv order by nufus_yogunlu asc;

select Bölge ,ülke , kýþýbaþý_alan from joucsv order by kýþýbaþý_alan desc;
select Bölge ,ülke , kýþýbaþý_alan from joucsv order by kýþýbaþý_alan asc;


select * from joucsv order by alan  desc;
select * from joucsv order by alan asc;

select * from joucsv  where Nüfus < 1000000;
select * from joucsv where  alan < 100000;
select * from joucsv where Bölge='Europe';
select * from joucsv where Bölge='Asia';
select * from joucsv where Bölge='Americas';

select * from joucsv where Para_birimi= 'USD'
select * from joucsv where Para_birimi='EUR';
select * from joucsv where bm=1;
select * from joucsv where Trafik_yönü='left'
select * from joucsv where Trafik_yönü='right'

select Bölge , avg(alan) as ortalama_alan from joucsv 
group by bölge order by ortalama_alan desc;

select Bölge , COUNT(*) as ülke_sayýsý from joucsv
group by Bölge order by ülke_sayýsý desc;

select Para_birimi , COUNT(*) as parabirimi_kullanýmý from joucsv
group by Para_birimi order by   Parabirimi_kullanýmý desc; 



