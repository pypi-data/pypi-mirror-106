if __name__ == "__main__":
    from fabric_cm.credmgr.credmgr_proxy import CredmgrProxy

    proxy = CredmgrProxy(credmgr_host="beta-2.fabric-testbed.net")
    response = proxy.refresh(project_name="all", scope="all",
                             refresh_token="NB2HI4DTHIXS6Y3JNRXWO33OFZXXEZZPN5QXK5DIGIXTINDDMEYWGMRRHFTDONZVG43GCNBZGE4WCMLCGNRTAMJXGAYDGNZ7OR4XAZJ5OJSWM4TFONUFI33LMVXCM5DTHUYTMMRRGI3TOMJRHE2DGNJGOZSXE43JN5XD25RSFYYCM3DJMZSXI2LNMU6TQNRUGAYDAMBQ")
    print(response)