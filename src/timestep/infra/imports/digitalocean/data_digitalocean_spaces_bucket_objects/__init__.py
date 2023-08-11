'''
# `data_digitalocean_spaces_bucket_objects`

Refer to the Terraform Registory for docs: [`data_digitalocean_spaces_bucket_objects`](https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class DataDigitaloceanSpacesBucketObjects(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="digitalocean.dataDigitaloceanSpacesBucketObjects.DataDigitaloceanSpacesBucketObjects",
):
    '''Represents a {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects digitalocean_spaces_bucket_objects}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        region: builtins.str,
        delimiter: typing.Optional[builtins.str] = None,
        encoding_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_keys: typing.Optional[jsii.Number] = None,
        prefix: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects digitalocean_spaces_bucket_objects} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#bucket DataDigitaloceanSpacesBucketObjects#bucket}.
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#region DataDigitaloceanSpacesBucketObjects#region}.
        :param delimiter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#delimiter DataDigitaloceanSpacesBucketObjects#delimiter}.
        :param encoding_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#encoding_type DataDigitaloceanSpacesBucketObjects#encoding_type}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#id DataDigitaloceanSpacesBucketObjects#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_keys: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#max_keys DataDigitaloceanSpacesBucketObjects#max_keys}.
        :param prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#prefix DataDigitaloceanSpacesBucketObjects#prefix}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba9d0d541b79b96d00d7457964f2a917422ee5395568e21ceb8ca1dd6306658d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDigitaloceanSpacesBucketObjectsConfig(
            bucket=bucket,
            region=region,
            delimiter=delimiter,
            encoding_type=encoding_type,
            id=id,
            max_keys=max_keys,
            prefix=prefix,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDelimiter")
    def reset_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelimiter", []))

    @jsii.member(jsii_name="resetEncodingType")
    def reset_encoding_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncodingType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxKeys")
    def reset_max_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxKeys", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="commonPrefixes")
    def common_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "commonPrefixes"))

    @builtins.property
    @jsii.member(jsii_name="keys")
    def keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keys"))

    @builtins.property
    @jsii.member(jsii_name="owners")
    def owners(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "owners"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="delimiterInput")
    def delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingTypeInput")
    def encoding_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxKeysInput")
    def max_keys_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__788c0d1c3ec8f047b6a1c20d16272adc3e8583aa3ebe58aed74d1eddf3b96ecf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="delimiter")
    def delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delimiter"))

    @delimiter.setter
    def delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974308881838c54d611f7ced539aba524bb077b007dbd231a9cbd01803e73fee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delimiter", value)

    @builtins.property
    @jsii.member(jsii_name="encodingType")
    def encoding_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encodingType"))

    @encoding_type.setter
    def encoding_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e2ae1878d2b24af16f1313ab9b1d17f20c3998ffad46e88e26e16f37d7ec506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encodingType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef1e3e59f18a0bb3acb9922c22a18a1c6af2d37422dff5895b42e5e3960d5aa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxKeys")
    def max_keys(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxKeys"))

    @max_keys.setter
    def max_keys(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa04bef1b76312015674f7b4ab3f8f5ba16f19f2a1d961cc729a0018c61cb5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxKeys", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a61922d4d032b4da70db0145d85a86696473417a37da4a1eed858d86497c83dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38929a470bc7699ad8622cde87153831af00ae762e72b320e0650fb3bb438317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="digitalocean.dataDigitaloceanSpacesBucketObjects.DataDigitaloceanSpacesBucketObjectsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "region": "region",
        "delimiter": "delimiter",
        "encoding_type": "encodingType",
        "id": "id",
        "max_keys": "maxKeys",
        "prefix": "prefix",
    },
)
class DataDigitaloceanSpacesBucketObjectsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        bucket: builtins.str,
        region: builtins.str,
        delimiter: typing.Optional[builtins.str] = None,
        encoding_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_keys: typing.Optional[jsii.Number] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#bucket DataDigitaloceanSpacesBucketObjects#bucket}.
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#region DataDigitaloceanSpacesBucketObjects#region}.
        :param delimiter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#delimiter DataDigitaloceanSpacesBucketObjects#delimiter}.
        :param encoding_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#encoding_type DataDigitaloceanSpacesBucketObjects#encoding_type}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#id DataDigitaloceanSpacesBucketObjects#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_keys: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#max_keys DataDigitaloceanSpacesBucketObjects#max_keys}.
        :param prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#prefix DataDigitaloceanSpacesBucketObjects#prefix}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5398aac6d601980386c5063a4e70d2eee6b43f8eda2ec6c71cd52adce9e47277)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
            check_type(argname="argument encoding_type", value=encoding_type, expected_type=type_hints["encoding_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_keys", value=max_keys, expected_type=type_hints["max_keys"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "region": region,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if delimiter is not None:
            self._values["delimiter"] = delimiter
        if encoding_type is not None:
            self._values["encoding_type"] = encoding_type
        if id is not None:
            self._values["id"] = id
        if max_keys is not None:
            self._values["max_keys"] = max_keys
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#bucket DataDigitaloceanSpacesBucketObjects#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#region DataDigitaloceanSpacesBucketObjects#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#delimiter DataDigitaloceanSpacesBucketObjects#delimiter}.'''
        result = self._values.get("delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encoding_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#encoding_type DataDigitaloceanSpacesBucketObjects#encoding_type}.'''
        result = self._values.get("encoding_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#id DataDigitaloceanSpacesBucketObjects#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_keys(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#max_keys DataDigitaloceanSpacesBucketObjects#max_keys}.'''
        result = self._values.get("max_keys")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/digitalocean/digitalocean/2.29.0/docs/data-sources/spaces_bucket_objects#prefix DataDigitaloceanSpacesBucketObjects#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDigitaloceanSpacesBucketObjectsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataDigitaloceanSpacesBucketObjects",
    "DataDigitaloceanSpacesBucketObjectsConfig",
]

publication.publish()

def _typecheckingstub__ba9d0d541b79b96d00d7457964f2a917422ee5395568e21ceb8ca1dd6306658d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    region: builtins.str,
    delimiter: typing.Optional[builtins.str] = None,
    encoding_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    max_keys: typing.Optional[jsii.Number] = None,
    prefix: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__788c0d1c3ec8f047b6a1c20d16272adc3e8583aa3ebe58aed74d1eddf3b96ecf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974308881838c54d611f7ced539aba524bb077b007dbd231a9cbd01803e73fee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e2ae1878d2b24af16f1313ab9b1d17f20c3998ffad46e88e26e16f37d7ec506(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1e3e59f18a0bb3acb9922c22a18a1c6af2d37422dff5895b42e5e3960d5aa5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa04bef1b76312015674f7b4ab3f8f5ba16f19f2a1d961cc729a0018c61cb5a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a61922d4d032b4da70db0145d85a86696473417a37da4a1eed858d86497c83dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38929a470bc7699ad8622cde87153831af00ae762e72b320e0650fb3bb438317(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5398aac6d601980386c5063a4e70d2eee6b43f8eda2ec6c71cd52adce9e47277(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    region: builtins.str,
    delimiter: typing.Optional[builtins.str] = None,
    encoding_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    max_keys: typing.Optional[jsii.Number] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
