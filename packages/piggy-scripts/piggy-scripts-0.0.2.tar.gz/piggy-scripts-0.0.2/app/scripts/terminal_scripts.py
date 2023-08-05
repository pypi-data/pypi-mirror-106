import pexpect


def configure_cloudhsm_client(EnIp):
    (output, exitstatus) = pexpect.run(
        'sudo service cloudhsm-client stop', withexitstatus=1)

    (output, exitstatus) = pexpect.run(
        f'sudo /opt/cloudhsm/bin/configure -a {EnIp}', withexitstatus=1)

    (output, exitstatus) = pexpect.run(
        'sudo service cloudhsm-client start', withexitstatus=1)

    (output, exitstatus) = pexpect.run(
        'sudo /opt/cloudhsm/bin/configure -m', withexitstatus=1)

    return


def move_customer_ca_cert():

    return
