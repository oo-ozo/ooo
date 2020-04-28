echo "Do you want to keep continue"
read -p "(Y=1, N=2)" B

if [ $B -eq 1 ]
then
	tput clear
	tput cup 6 15
        tput setaf 87
	echo "Welcom to facebook hacking"
	sh hack.sh
else
	tput clear
        tput cup 6 15
        tput setaf 87
	echo "Have a nice day"
fi
