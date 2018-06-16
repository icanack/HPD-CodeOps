package "telnet" 



package "wget"



package "vim"


directory "/opt/hpd" do
 owner 'root'
 group 'root'
 mode '0755'
 action :create
end


cron "testes hpd" do
  minute '0'
  hour   '0'
  weekday '1'
  user 'root'
  command 'ls -l'
  action :delete
end

user 'ricardo' do
 home '/home/ricardo'
 password '11541asasdsa$asda123%**'
 action :create
 manage_home true
end


execute "Download do chef-dk" do
  command "cd /opt/hpd && wget https://packages.chef.io/files/stable/chefdk/3.0.36/el/7/chefdk-3.0.36-1.el7.x86_64.rpm"
end
