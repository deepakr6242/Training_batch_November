icto_common:
  env: sit2
  domain: 1dc.com
  user: root
  group: root
  repo_url: http://10.92.8.236:8081/repository/salt-files/com/firstdata
  run_dir: /srv/runs
  service_dir: /etc/systemd/system
  log_dir: /srv/log
  ip_address: {{ grains['ip_interfaces']['eth0'][0] }}

icto_dsee7:
  repo_url: http://10.92.8.236:8081/repository/salt-dev/com/firstdata/files/openldap
  archive_name: dsee7.tar.gz
  install_dir: /opt/scripts/bash_setup/firstdata-master/server-setup/deploy/software/
  internal_ldif: internal_only.ldif
  external_ldif: external_internal.ldif

icto_ldap:
  base_dir: /opt/scripts/bash_setup/firstdata-master
  hostnames:
    - aplus1
    - aplus2
  masters:
    - aplus1
    - aplus2
  consumers: []

icto_openam:
  instance: openam_s01
  deploy_url: http://10.92.8.236:8081/repository/salt-dev/com/firstdata/files/openam/
  deploy_name: deployOpenAM.zip
  deploy_dir: /appserver/openam/source/APP_SERVER/OPENAM-11.0.0/Scripts/

icto_jdk:
  repo_url: http://10.92.8.236:8081/repository/salt-files/com/firstdata/java/
  archive_name: jdk-8u181-linux-x64.tar.gz
  install_dir: /opt
  name: jdk1.8.0_181

icto_wildfly:
  repo_url: http://10.92.8.236:8081/repository/salt-dev/com/firstdata/files/wildfly
  archive_name: DSWEB-wildfly-10.1.0.Final.zip
  admin_name: admin_jboss.zip
  admin_dir: /appserver/admin/bin
  name: wildfly-10.1.0.Final
  user: websrvr
icto_cc:
  instances:
    cc1_r2_s01:
      storepass:
      keypass:
      release: 20.08.04.00demo
  global_name: com.firstdata.configuration
  war_file: FDAPlusCCWeb.war
  modules:
    - async.properties
    - auditingGateway.properties
    - config.properties
    - context.properties
    - ErrorConfig.properties
    - ficsServices.properties
    - firstpayservices.properties
    - log4j.dtd
    - log4j.xml
    - log4j.xml_orig
    - module.xml
    - oscache.properties
    - postcodeDetails.properties
    - process.properties
    - validation.properties
    - VMxUtilities.properties
  COPYBOOK_PATH:
  EE_hostname:
  EE_port:
  EE_server_URL:
  EE_wsdl_URL:
  ENV_URL:
  Firstpay_service_URL:
  IP_ADDRESS:
  JBOSS_LOG_DIR:
  POSTCODE_CONNECTION_URL:
  SSO_CookieName:

icto_ee:
  instances:
    eewebtop_c01:
      storepass: P4ssw0rd
      keypass: eGDZ3plD2
      deploy:


icto_aa:
  instances:
    eewebtop_c01:
      release: 123.230.89.36
      storepass: P4ssw0rd
      keypass: eGDZ3plD2
      deploy: