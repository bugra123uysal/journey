select * from journee;

select �lke , B�lge from journee;
select �lke , alan from journee;
select �lke , d�viz_fiyat� from journee;
select �lke , N�fus from journee;
select �lke , Ba�kent from journee;
select �lke , Trafik_y�n� from journee;
select B�lge , Trafik_y�n� from journee;

select * from journee order by  N�fus desc;
select * from journee order by N�fus asc ;

select * from journee order by alan  desc;
select * from journee order by alan asc;

select * from journee  where N�fus < 1000000;
select * from journee where  alan < 100000;
select * from journee where B�lge='Europe';
select * from journee where B�lge='Asia';
select * from journee where B�lge='Americas';

select * from journee where Para_birimi= 'USD'
select * from journee where Para_birimi='EUR';
select * from journee where bm=1;
select * from journee where Trafik_y�n�='left'
select * from journee where Trafik_y�n�='right'






