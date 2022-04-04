# Simple Password Message Encrypt/Decrypt

## Usage

clone the repo and cd into it. It's recommended to create a virtualenv before you move on.

install the requirements

```shell
pip install -r requirements.txt
```

### To encrypt a message

```shell
$ python encrypt.py
> Enter message to encrypt: <Enter the message you wat to encrypt>
> Enter a password: <Your Password>
> Repeate your password: <Your Password>
S2R0B3sbK3Qk57ZCmzJP2wABhqCAAAAAAGJKhOm2tlFUH80QOub_mh7OtdWMx3HOwzpoRvreueemH0L8brJihH_dALM_ZsCaICIDSzFWQh5QDaHVxXKcRWfJ9auvGz0ppQ3xEXklmZzPUxxjj_qQpPBKoi8l2ovoqspw2Bs=
```

### To decrypt a token

```shell
$ python decrypt.py
> Enter Encrypted Message: S2R0B3sbK3Qk57ZCmzJP2wABhqCAAAAAAGJKhOm2tlFUH80QOub_mh7OtdWMx3HOwzpoRvreueemH0L8brJihH_dALM_ZsCaICIDSzFWQh5QDaHVxXKcRWfJ9auvGz0ppQ3xEXklmZzPUxxjj_qQpPBKoi8l2ovoqspw2Bs=
> Enter a password: <Your Password>
```
