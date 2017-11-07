/**
 * main.js 파일
 */

$(document).ready(function(){
	//form element object 
	//사용자가 전송 버튼을 클릭하면 등록된 콜백함수가 호출
	$('#search').on('submit', function(event){
		console.log($('#search').serialize());
		event.preventDefault();
		$.ajax({
			url:'/search',
			type:'POST',
			dataType:'json',
			// serialize 키:값 형태
			data:$('#search').serialize(),
			success:function(team){
				var html = "";
					html+= "<tr>";
					html+= "<th><strong>"+team.id+"</strong></th>";
					html+= "<td class='tm'>";
					html+= "   <div>";
					html+= "       <span id='team_HT'>"+team.name+"</span>";
					html+= "    </div>";
					html+= "</td>";
					html+= "<td><span>"+team.play+"</span></td>";
					html+= "<td><span>"+team.w+"</span></td>";
					html+= "<td><span>"+team.l+"</span></td>";
					html+= "<td><span>"+team.d+"</span></td>";
					html+= "<td><strong>"+team.win+"</strong></td>";
					html+= "<td><span>"+team.etc1+"</span></td>";
					html+= "<td><span>"+team.etc2+"</span></td>";
					html+= "<td><span>"+team.etc3+"</span></td>";
					html+= "<td><span>"+team.etc4+"</span></td>";
					html+= "<td class='last'><span>"+team.etc5+"</span></td>";
					html+= "</tr>";
					$('#resultTable').append(html);
					$('input[name=keyword]').val("");
			},
			error:function(e){
				console.log('에러', e)
			}
		});
		return false;
	})
})