select * from joucsv;

select �lke , B�lge from joucsv;
select �lke , alan from joucsv;
select �lke , d�viz_fiyat� from joucsv;
select �lke , N�fus from joucsv;
select �lke , Ba�kent from joucsv;
select �lke , Trafik_y�n� from joucsv;
select B�lge , Trafik_y�n� from joucsv;
select �lke , nufus_yogunlu from joucsv ;

select �lke , k���ba��_alan from joucsv;

select * from joucsv order by  N�fus desc;
select * from joucsv order by N�fus asc ;

select B�lge, �lke , nufus_yogunlu from joucsv order by nufus_yogunlu desc;
select B�lge ,�lke , nufus_yogunlu from joucsv order by nufus_yogunlu asc;

select B�lge ,�lke , k���ba��_alan from joucsv order by k���ba��_alan desc;
select B�lge ,�lke , k���ba��_alan from joucsv order by k���ba��_alan asc;


select * from joucsv order by alan  desc;
select * from joucsv order by alan asc;

select * from joucsv  where N�fus < 1000000;
select * from joucsv where  alan < 100000;
select * from joucsv where B�lge='Europe';
select * from joucsv where B�lge='Asia';
select * from joucsv where B�lge='Americas';

select * from joucsv where Para_birimi= 'USD'
select * from joucsv where Para_birimi='EUR';
select * from joucsv where bm=1;
select * from joucsv where Trafik_y�n�='left'
select * from joucsv where Trafik_y�n�='right'

select B�lge , avg(alan) as ortalama_alan from joucsv 
group by b�lge order by ortalama_alan desc;

select B�lge , COUNT(*) as �lke_say�s� from joucsv
group by B�lge order by �lke_say�s� desc;

select Para_birimi , COUNT(*) as parabirimi_kullan�m� from joucsv
group by Para_birimi order by   Parabirimi_kullan�m� desc; 



