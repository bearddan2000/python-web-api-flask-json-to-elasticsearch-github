#!/usr/bin/env bash
basefile="install"
logfile="general.log"
timestamp=`date '+%Y-%m-%d %H:%M:%S'`

if [ "$#" -ne 1 ]; then
  msg="[ERROR]: $basefile failed to receive enough args"
  echo "$msg"
  echo "$msg" >> $logfile
  exit 1
fi

function setup-logging(){
  scope="setup-logging"
  info_base="[$timestamp INFO]: $basefile::$scope"

  echo "$info_base started" >> $logfile

  echo "$info_base removing old logs" >> $logfile

  rm -f $logfile

  echo "$info_base ended" >> $logfile

  echo "================" >> $logfile
}

function root-check(){
  scope="root-check"
  info_base="[$timestamp INFO]: $basefile::$scope"

  echo "$info_base started" >> $logfile

  #Make sure the script is running as root.
  if [ "$UID" -ne "0" ]; then
    echo "[$timestamp ERROR]: $basefile::$scope you must be root to run $0" >> $logfile
    echo "==================" >> $logfile
    echo "You must be root to run $0. Try the following"
    echo "sudo $0"
    exit 1
  fi

  echo "$info_base ended" >> $logfile
  echo "================" >> $logfile
}

function docker-check() {
  scope="docker-check"
  info_base="[$timestamp INFO]: $basefile::$scope"
  cmd=`docker -v`

  echo "$info_base started" >> $logfile

  if [ -z "$cmd" ]; then
    echo "$info_base docker not installed"
    echo "$info_base docker not installed" >> $logfile
  fi

  echo "$info_base ended" >> $logfile
  echo "================" >> $logfile

}

function docker-compose-check() {
  scope="docker-compose-check"
  info_base="[$timestamp INFO]: $basefile::$scope"
  cmd=`docker-compose -v`

  echo "$info_base started" >> $logfile

  if [ -z "$cmd" ]; then
    echo "$info_base docker-compose not installed"
    echo "$info_base docker-compose not installed" >> $logfile
  fi

  echo "$info_base ended" >> $logfile
  echo "================" >> $logfile

}

function usage() {
    echo ""
    echo "Usage: "
    echo ""
    echo "-u: start."
    echo "-d: tear down."
    echo "-h: Display this help and exit."
    echo ""
}

function create-repo-list() {
  local docker_img_tag="download"
  local docker_img_name="download"
  local services="py-srv"
  local target_dir="app/Repo.csv"

  rm -Rf "$(pwd)/$docker_img_tag/$target_dir"

  sudo docker build -t $docker_img_tag $(pwd)/$docker_img_tag

  sudo docker run -t --name $docker_img_name $docker_img_tag

  sudo docker cp $docker_img_name:/$target_dir $(pwd)/$docker_img_tag

  sudo docker stop $docker_img_name

  sudo docker rm $docker_img_name

  cp -R "$(pwd)/$docker_img_tag/$target_dir" "$(pwd)/$services/bin/$target_dir"

}
function remove-repo-list() {
  local docker_img_tag="download"
  local services="py-srv"
  local target_dir="app/Repo.csv"

  rm -Rf "$(pwd)/$docker_img_tag/$target_dir"
}

function create-process-repo() {
  local docker_img_tag="process"
  local docker_img_name="process"
  local services="py-srv"
  local target_dir="app/data.txt"

  rm -Rf "$(pwd)/$docker_img_tag/$target_dir"

  sudo docker build -t $docker_img_tag $(pwd)/$docker_img_tag

  sudo docker run -t --name $docker_img_name $docker_img_tag

  sudo docker cp $docker_img_name:/$target_dir $(pwd)/$docker_img_tag

  sudo docker stop $docker_img_name

  sudo docker rm $docker_img_name

  cp -R "$(pwd)/$docker_img_tag/$target_dir" "$(pwd)/$services/bin/$target_dir"

}
function remove-process-repo() {
  local docker_img_tag="process"
  local services="py-srv"
  local target_dir="app/data.txt"

  rm -Rf "$(pwd)/$docker_img_tag/$target_dir"
}
function create-certs() {
  local docker_img_tag=$1
  local docker_img_name=$2
  local services=$3
  local target_dir=$4

  rm -Rf "$(pwd)/$docker_img_tag/$target_dir"

  sudo docker build -t $docker_img_tag $(pwd)/$docker_img_tag

  sudo docker run -d --name $docker_img_name $docker_img_tag

  sudo docker cp $docker_img_name:/$target_dir $(pwd)/$docker_img_tag

  sudo docker rm $docker_img_name

  for d in `echo $services | awk '{print $0}'`; do
    #statements
    cp -R "$(pwd)/$docker_img_tag/$target_dir" "$(pwd)/$d"
  done

}
function remove-certs() {
  local docker_img_tag=$1
  local services=$2
  local target_dir=$3

  rm -Rf "$(pwd)/$docker_img_tag/$target_dir"

  rm -Rf "$(pwd)/$d/$target_dir"

}
function start-up(){

    local scope="start-up"
    local docker_img_name=`head -n 1 README.md | sed 's/# //'`
    local info_base="[$timestamp INFO]: $basefile::$scope"

    echo "$info_base started" >> $logfile

    echo "$info_base starting services" >> $logfile

 #  create-process-repo

 #   create-repo-list

    sudo docker-compose up --build

    echo "$info_base ended" >> $logfile

    echo "================" >> $logfile
}
function tear-down(){

    scope="tear-down"
    info_base="[$timestamp INFO]: $basefile::$scope"

    echo "$info_base started" >> $logfile

    echo "$info_base starting services" >> $logfile

#    remove-process-repo

#    remove-repo-list

    sudo docker-compose down

    echo "$info_base ended" >> $logfile

    echo "================" >> $logfile
}

root-check
docker-check
docker-compose-check

while getopts ":udh" opts; do
  case $opts in
    u)
      setup-logging
      start-up ;;
    d)
      tear-down ;;
    h)
      usage
      exit 0 ;;
    /?)
      usage
      exit 1 ;;
  esac
done
