//엘리먼트들에 대한 데이터를 테이블 형식으로 화면에 표현하기

function makeTable(elem){
	var $table = $("<table border=1>"); // <table border=1>태그를 생성하는 변수 $table을 선언
	
	//컬럼 정의하기
	for(var i =0; i<1;i++){				// for문 조건식 : i가 0이고, i에 1씩 더할 건데 i의 범위가 1 미만일때까지 반복
		var $tr=$("<tr>");				// <tr>태그 생성하는 변수 $tr 선언
		for(var j=0; j<elem.eq(0).children().length;j++){
			// for문 조건식 : j가 0이고, i에 1씩 더할 건데 j 함수 makeTable의 매개변수로 들어간 값의 첫번째 태그의 자식 태그들의 개수(몇 개의 자식 태그가 있는지)보다 작을 때까지 반복
			var $td=$("<td>").append(elem.eq(0).children().eq(j).prop("tagName"));
			// <td>라는 태그를 만들고 makeTable의 매개변수로 들어간 값의 첫번째 태그의 j번째 자식 태그에 tagName 속성을 줌
			$tr.append($td);	// $tr의 자식요소에 $td를 추가
		}
		$table.append($tr);		// $table의 자식요소에 $tr를 추가
	}
	
	//데이터 넣기
	for(var i =0; i<elem.length;i++){ // for문 조건식 : i는 0이고, i에 1씩 더해줄건데 함수 makeTable에 넣은 값의 길이 미만일때까지 반복
		var $tr=$("<tr>");			// <tr>태그를 생성하는 변수 $tr 선언
		for(var j=0; j<elem.eq(i).children().length;j++){  // j는 0이고 j에 1씩 더해줄건데 함수 makeTable에 넣은 값의 i번째 자식태그의 길이만큼 반복
			var $td=$("<td>").append(elem.eq(i).children().eq(j).text());
			$tr.append($td);	// $tr의 자식요소에 $td를 추가
		}
		$table.append($tr);	// $table의 자식요소에 $tr를 추가
	}
	
	//만들어진 테이블 반환
	return $table;
}



