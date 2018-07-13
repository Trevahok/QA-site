var cnt=1;
            function change()
            {
                console.log(cnt);
                var root=document.getElementById('background');
                root.className='bg'+cnt;
                var render=document.getElementById('render');
                render.className='bg'+(cnt+1);
                cnt=(cnt<5)?cnt+1:1;
            }
            setInterval(change,5000);
			function validatepass()
			{
				var str=document.getElementById('password').value;
				if(str.length>=8)
				{
					document.getElementById('pfalse').style.visibility="hidden";
					document.getElementById('ptrue').style.visibility="visible";

				}
				else{
					document.getElementById('ptrue').style.visibility="hidden";
					document.getElementById('pfalse').style.visibility="visible";

				}
			}
			function validatecpass()
			{
				var str=document.getElementById('password').value;
				var str2=document.getElementById('cpassword').value;
				if(str==str2)
				{
					document.getElementById('cfalse').style.visibility="hidden";
					document.getElementById('ctrue').style.visibility="visible";

				}
				else{
					document.getElementById('ctrue').style.visibility="hidden";
					document.getElementById('cfalse').style.visibility="visible";

				}
			}
