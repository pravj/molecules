<?php

/*
microsoft Hackcon-2014
*/

	include('simple_html_dom.php');

	$main = "http://hackcon14.cloudapp.net:8080/";

	$yay = "";

	$html = file_get_html($main);

	foreach ($html->find('a') as $a) {
		$yay = "".$main."".$a->href."";
	}


	function steps($url)
	{
		$data = file_get_html($url);

		foreach($data->find('a') as $l)
		{
			if(strpos($l->href, '@'))
			{
				echo $l->href;
				echo "</br>";
			}
			else
			{
				//echo ("http://hackcon14.cloudapp.net:8080/Pages/".$l->href."");
				steps("http://hackcon14.cloudapp.net:8080/Pages/".$l->href."");
			}
		}
	}

	steps($yay);

	/*
	Python version of same using BeautifulSoup

	from bs4 import BeautifulSoup
	import urllib2

	main = "http://hackcon14.cloudapp.net:8080/"
	yay = "http://hackcon14.cloudapp.net:8080/Pages/06ccdff2-24d.html"

	def steps(url):
		data = urllib2.urlopen(url).read()
		soup = BeautifulSoup(data)

		links = soup.find_all('a')
		for link in links:
			href = link.get('href')
			if (href.index('@') != 0):
				print href
			else:
				steps("http://hackcon14.cloudapp.net:8080/Pages/" + href)

	steps(yay)
	*/
	
?>




