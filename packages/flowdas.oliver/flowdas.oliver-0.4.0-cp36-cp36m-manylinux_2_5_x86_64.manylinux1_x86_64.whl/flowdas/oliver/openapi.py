# coding=utf-8
# Copyright 2017 Flowdas Inc. <prospero@flowdas.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""OpenAPI Sepcification 3.0
"""
from flowdas.meta.property import Container

from flowdas import meta


class Object(Container):
    pass


@meta.declare
class Info:
    pass


@meta.declare
class Contact:
    pass


@meta.declare
class License:
    pass


@meta.declare
class Server:
    pass


@meta.declare
class ServerVariable:
    pass


@meta.declare
class Components:
    pass


@meta.declare
class PathItem:
    pass


@meta.declare
class Operation:
    pass


@meta.declare
class ExternalDocumentation:
    pass


@meta.declare
class Parameter:
    pass


@meta.declare
class RequestBody:
    pass


@meta.declare
class MediaType:
    pass


@meta.declare
class Encoding:
    pass


@meta.declare
class Response:
    pass


@meta.declare
class Example:
    pass


@meta.declare
class Link:
    pass


@meta.declare
class Header:
    pass


@meta.declare
class Tag:
    pass


@meta.declare
class Schema:
    pass


@meta.declare
class Discriminator:
    pass


@meta.declare
class XML:
    pass


@meta.declare
class SecurityScheme:
    pass


@meta.declare
class OAuthFlows:
    pass


@meta.declare
class OAuthFlow:
    pass


class Reference(meta.Entity):
    _ref = meta.String(name='$ref')


class OpenAPI(meta.Entity):
    openapi = meta.String()
    info = Info()
    servers = Server[:]()
    paths = Object(PathItem())
    components = Components()
    security = meta.Tuple(Object(meta.String[:]()), repeat=slice(None))
    tags = Tag[:]()
    externalDocs = ExternalDocumentation()

    _resolved = False

    def resolve(self):
        if self._resolved:
            return
        # TODO
        self._resolved = True

    def install(self, app):
        for uri_template in (self.paths or {}):
            path = self.paths[uri_template]


class Info(meta.Entity):
    title = meta.String()
    description = meta.String()
    termsOfService = meta.String()
    contact = Contact()
    license = License()
    version = meta.String()


class Contact(meta.Entity):
    name = meta.String()
    url = meta.String()
    email = meta.String()


class License(meta.Entity):
    name = meta.String()
    url = meta.String()


class Server(meta.Entity):
    url = meta.String()
    description = meta.String()
    variables = Object(ServerVariable())


class ServerVariable(meta.Entity):
    enum = meta.String[:]()
    default = meta.String()
    description = meta.String()


class Components(meta.Entity):
    schemas = Object(Schema())
    responses = Object(Response())
    parameters = Object(Parameter())
    examples = Object(Example())
    requestBodies = Object(RequestBody())
    headers = Object(Header())
    securitySchemes = Object(SecurityScheme())
    links = Object(Link())
    callbacks = Object(Object(PathItem()))


class PathItem(meta.Entity):
    _ref = meta.String(name='$ref')
    summary = meta.String()
    description = meta.String()
    get = Operation()
    put = Operation()
    post = Operation()
    delete = Operation()
    options = Operation()
    head = Operation()
    patch = Operation()
    trace = Operation()
    servers = Server[:]()
    parameters = Parameter()


class Operation(meta.Entity):
    tags = meta.String[:]()
    summary = meta.String()
    description = meta.String()
    externalDocs = ExternalDocumentation()
    operationId = meta.String()
    parameters = Parameter[:]()
    requestBody = RequestBody()
    responses = Object(Response())
    callbacks = Object(Object(PathItem()))
    deprecated = meta.Boolean()
    security = meta.Tuple(Object(meta.String[:]()), repeat=slice(None))
    servers = Server[:]()


class ExternalDocumentation(meta.Entity):
    description = meta.String()
    url = meta.String()


class Parameter(Reference):
    name = meta.String()
    in_ = meta.String(name='in')
    description = meta.String()
    required = meta.Boolean()
    deprecated = meta.Boolean()
    allowEmptyValue = meta.Boolean()
    style = meta.String()
    explode = meta.Boolean()
    allowReserved = meta.Boolean()
    schema = Schema()
    example = meta.Primitive()
    examples = Object(Example())
    content = Object(MediaType())


class RequestBody(Reference):
    description = meta.String()
    content = Object(MediaType())
    required = meta.Boolean()


class MediaType(meta.Entity):
    schema = Schema()
    example = meta.Primitive()
    examples = Object(Example())
    encoding = Object(Encoding())


class Encoding(meta.Entity):
    contentType = meta.String()
    headers = Object(Header())
    style = meta.String()
    explode = meta.Boolean()
    allowReserved = meta.Boolean()


class Response(Reference):
    description = meta.String()
    headers = Object(Header())
    content = Object(MediaType())
    links = Object(Link())


class Example(Reference):
    summary = meta.String()
    description = meta.String()
    value = meta.Primitive()
    externalValue = meta.String()


class Link(Reference):
    operationRef = meta.String()
    operationId = meta.String()
    parameters = meta.JsonObject()
    requestBody = meta.Primitive()
    description = meta.String()
    server = Server()


class Header(Reference):
    description = meta.String()
    required = meta.Boolean()
    deprecated = meta.Boolean()
    allowEmptyValue = meta.Boolean()
    style = meta.String()
    explode = meta.Boolean()
    allowReserved = meta.Boolean()
    schema = Schema()
    example = meta.Primitive()
    examples = Object(Example())
    content = Object(MediaType())


class Tag(meta.Entity):
    name = meta.String()
    description = meta.String()
    externalDocs = ExternalDocumentation()


class SchemaItems(meta.Union):
    many = Schema[1:]()
    mono = Schema()


class SchemaDependency(meta.Union):
    many = meta.String[:]()
    mono = Schema()


class SchemaType(meta.Union):
    many = meta.String[:]()
    mono = meta.String()


class Schema(Reference):
    _schema = meta.String(name='$schema')
    _id = meta.String(name='$id')
    id = meta.String()
    title = meta.String()
    description = meta.String()
    default = meta.Primitive()
    multipleOf = meta.Number()
    maximum = meta.Number()
    exclusiveMaximum = meta.Number()
    minimum = meta.Number()
    exclusiveMinimum = meta.Number()
    maxLength = meta.Integer()
    minLength = meta.Integer()
    pattern = meta.String()
    additionalItems = Schema()
    items = SchemaItems()
    maxItems = meta.Integer()
    minItems = meta.Integer()
    uniqueItems = meta.Boolean()
    contains = Schema()
    maxProperties = meta.Integer()
    minProperties = meta.Integer()
    required = meta.String[:]()
    additionalProperties = Schema()
    definitions = Object(Schema())
    properties = Object(Schema())
    patternProperties = Object(Schema())
    dependencies = Object(SchemaDependency())
    propertyNames = Schema()
    const = meta.Primitive()
    enum = meta.JsonArray()
    type = SchemaType()
    format = meta.String()
    allOf = Schema[1:]()
    anyOf = Schema[1:]()
    oneOf = Schema[1:]()
    not_ = Schema(name='not')

    nullable = meta.Boolean()
    discriminator = Discriminator()
    readOnly = meta.Boolean()
    writeOnly = meta.Boolean()
    xml = XML()
    externalDocs = ExternalDocumentation()
    example = meta.Primitive()
    deprecated = meta.Boolean()


class Discriminator(meta.Entity):
    propertyName = meta.String()
    mapping = Object(meta.String())


class XML(meta.Entity):
    name = meta.String()
    namespace = meta.String()
    prefix = meta.String()
    attribute = meta.Boolean()
    wrapped = meta.Boolean()


class SecurityScheme(Reference):
    type = meta.String()
    description = meta.String()
    name = meta.String()
    in_ = meta.String()
    scheme = meta.String()
    bearerFormat = meta.String()
    flows = OAuthFlows()
    openIdConnectUrl = meta.String()


class OAuthFlows(meta.Entity):
    implicit = OAuthFlow()
    password = OAuthFlow()
    clientCredentials = OAuthFlow()
    authorizationCode = OAuthFlow()


class OAuthFlow(meta.Entity):
    authorizationUrl = meta.String()
    tokenUrl = meta.String()
    refreshUrl = meta.String()
    scopes = Object(meta.String())
