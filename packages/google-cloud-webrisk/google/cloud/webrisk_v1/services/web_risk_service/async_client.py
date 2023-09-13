# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.webrisk_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.webrisk_v1.types import webrisk

from .client import WebRiskServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, WebRiskServiceTransport
from .transports.grpc_asyncio import WebRiskServiceGrpcAsyncIOTransport


class WebRiskServiceAsyncClient:
    """Web Risk API defines an interface to detect malicious URLs on
    your website and in client applications.
    """

    _client: WebRiskServiceClient

    DEFAULT_ENDPOINT = WebRiskServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = WebRiskServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        WebRiskServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        WebRiskServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(WebRiskServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        WebRiskServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        WebRiskServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        WebRiskServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(WebRiskServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        WebRiskServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(WebRiskServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        WebRiskServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WebRiskServiceAsyncClient: The constructed client.
        """
        return WebRiskServiceClient.from_service_account_info.__func__(WebRiskServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WebRiskServiceAsyncClient: The constructed client.
        """
        return WebRiskServiceClient.from_service_account_file.__func__(WebRiskServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return WebRiskServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> WebRiskServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            WebRiskServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(WebRiskServiceClient).get_transport_class, type(WebRiskServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, WebRiskServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the web risk service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.WebRiskServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = WebRiskServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def compute_threat_list_diff(
        self,
        request: Optional[Union[webrisk.ComputeThreatListDiffRequest, dict]] = None,
        *,
        threat_type: Optional[webrisk.ThreatType] = None,
        version_token: Optional[bytes] = None,
        constraints: Optional[webrisk.ComputeThreatListDiffRequest.Constraints] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> webrisk.ComputeThreatListDiffResponse:
        r"""Gets the most recent threat list diffs. These diffs
        should be applied to a local database of hashes to keep
        it up-to-date. If the local database is empty or
        excessively out-of-date, a complete snapshot of the
        database will be returned. This Method only updates a
        single ThreatList at a time. To update multiple
        ThreatList databases, this method needs to be called
        once for each list.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import webrisk_v1

            async def sample_compute_threat_list_diff():
                # Create a client
                client = webrisk_v1.WebRiskServiceAsyncClient()

                # Initialize request argument(s)
                request = webrisk_v1.ComputeThreatListDiffRequest(
                    threat_type="SOCIAL_ENGINEERING_EXTENDED_COVERAGE",
                )

                # Make the request
                response = await client.compute_threat_list_diff(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.webrisk_v1.types.ComputeThreatListDiffRequest, dict]]):
                The request object. Describes an API diff request.
            threat_type (:class:`google.cloud.webrisk_v1.types.ThreatType`):
                Required. The threat list to update.
                Only a single ThreatType should be
                specified per request. If you want to
                handle multiple ThreatTypes, you must
                make one request per ThreatType.

                This corresponds to the ``threat_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            version_token (:class:`bytes`):
                The current version token of the
                client for the requested list (the
                client version that was received from
                the last successful diff). If the client
                does not have a version token (this is
                the first time calling
                ComputeThreatListDiff), this may be left
                empty and a full database snapshot will
                be returned.

                This corresponds to the ``version_token`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            constraints (:class:`google.cloud.webrisk_v1.types.ComputeThreatListDiffRequest.Constraints`):
                Required. The constraints associated
                with this request.

                This corresponds to the ``constraints`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.webrisk_v1.types.ComputeThreatListDiffResponse:

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([threat_type, version_token, constraints])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = webrisk.ComputeThreatListDiffRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if threat_type is not None:
            request.threat_type = threat_type
        if version_token is not None:
            request.version_token = version_token
        if constraints is not None:
            request.constraints = constraints

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.compute_threat_list_diff,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_uris(
        self,
        request: Optional[Union[webrisk.SearchUrisRequest, dict]] = None,
        *,
        uri: Optional[str] = None,
        threat_types: Optional[MutableSequence[webrisk.ThreatType]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> webrisk.SearchUrisResponse:
        r"""This method is used to check whether a URI is on a
        given threatList. Multiple threatLists may be searched
        in a single query. The response will list all requested
        threatLists the URI was found to match. If the URI is
        not found on any of the requested ThreatList an empty
        response will be returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import webrisk_v1

            async def sample_search_uris():
                # Create a client
                client = webrisk_v1.WebRiskServiceAsyncClient()

                # Initialize request argument(s)
                request = webrisk_v1.SearchUrisRequest(
                    uri="uri_value",
                    threat_types=['SOCIAL_ENGINEERING_EXTENDED_COVERAGE'],
                )

                # Make the request
                response = await client.search_uris(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.webrisk_v1.types.SearchUrisRequest, dict]]):
                The request object. Request to check URI entries against
                threatLists.
            uri (:class:`str`):
                Required. The URI to be checked for
                matches.

                This corresponds to the ``uri`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            threat_types (:class:`MutableSequence[google.cloud.webrisk_v1.types.ThreatType]`):
                Required. The ThreatLists to search
                in. Multiple ThreatLists may be
                specified.

                This corresponds to the ``threat_types`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.webrisk_v1.types.SearchUrisResponse:

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([uri, threat_types])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = webrisk.SearchUrisRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if uri is not None:
            request.uri = uri
        if threat_types:
            request.threat_types.extend(threat_types)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search_uris,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_hashes(
        self,
        request: Optional[Union[webrisk.SearchHashesRequest, dict]] = None,
        *,
        hash_prefix: Optional[bytes] = None,
        threat_types: Optional[MutableSequence[webrisk.ThreatType]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> webrisk.SearchHashesResponse:
        r"""Gets the full hashes that match the requested hash
        prefix. This is used after a hash prefix is looked up in
        a threatList and there is a match. The client side
        threatList only holds partial hashes so the client must
        query this method to determine if there is a full hash
        match of a threat.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import webrisk_v1

            async def sample_search_hashes():
                # Create a client
                client = webrisk_v1.WebRiskServiceAsyncClient()

                # Initialize request argument(s)
                request = webrisk_v1.SearchHashesRequest(
                    threat_types=['SOCIAL_ENGINEERING_EXTENDED_COVERAGE'],
                )

                # Make the request
                response = await client.search_hashes(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.webrisk_v1.types.SearchHashesRequest, dict]]):
                The request object. Request to return full hashes matched
                by the provided hash prefixes.
            hash_prefix (:class:`bytes`):
                A hash prefix, consisting of the most
                significant 4-32 bytes of a SHA256 hash.
                For JSON requests, this field is
                base64-encoded. Note that if this
                parameter is provided by a URI, it must
                be encoded using the web safe base64
                variant (RFC 4648).

                This corresponds to the ``hash_prefix`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            threat_types (:class:`MutableSequence[google.cloud.webrisk_v1.types.ThreatType]`):
                Required. The ThreatLists to search
                in. Multiple ThreatLists may be
                specified.

                This corresponds to the ``threat_types`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.webrisk_v1.types.SearchHashesResponse:

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([hash_prefix, threat_types])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = webrisk.SearchHashesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if hash_prefix is not None:
            request.hash_prefix = hash_prefix
        if threat_types:
            request.threat_types.extend(threat_types)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.search_hashes,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_submission(
        self,
        request: Optional[Union[webrisk.CreateSubmissionRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        submission: Optional[webrisk.Submission] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> webrisk.Submission:
        r"""Creates a Submission of a URI suspected of containing phishing
        content to be reviewed. If the result verifies the existence of
        malicious phishing content, the site will be added to the
        `Google's Social Engineering
        lists <https://support.google.com/webmasters/answer/6350487/>`__
        in order to protect users that could get exposed to this threat
        in the future. Only allowlisted projects can use this method
        during Early Access. Please reach out to Sales or your customer
        engineer to obtain access.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import webrisk_v1

            async def sample_create_submission():
                # Create a client
                client = webrisk_v1.WebRiskServiceAsyncClient()

                # Initialize request argument(s)
                submission = webrisk_v1.Submission()
                submission.uri = "uri_value"

                request = webrisk_v1.CreateSubmissionRequest(
                    parent="parent_value",
                    submission=submission,
                )

                # Make the request
                response = await client.create_submission(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.webrisk_v1.types.CreateSubmissionRequest, dict]]):
                The request object. Request to send a potentially phishy
                URI to WebRisk.
            parent (:class:`str`):
                Required. The name of the project that is making the
                submission. This string is in the format
                "projects/{project_number}".

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            submission (:class:`google.cloud.webrisk_v1.types.Submission`):
                Required. The submission that
                contains the content of the phishing
                report.

                This corresponds to the ``submission`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.webrisk_v1.types.Submission:
                Wraps a URI that might be displaying
                malicious content.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, submission])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = webrisk.CreateSubmissionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if submission is not None:
            request.submission = submission

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_submission,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def submit_uri(
        self,
        request: Optional[Union[webrisk.SubmitUriRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Submits a URI suspected of containing malicious content to be
        reviewed. Returns a google.longrunning.Operation which, once the
        review is complete, is updated with its result. You can use the
        [Pub/Sub API] (https://cloud.google.com/pubsub) to receive
        notifications for the returned Operation. If the result verifies
        the existence of malicious content, the site will be added to
        the [Google's Social Engineering lists]
        (https://support.google.com/webmasters/answer/6350487/) in order
        to protect users that could get exposed to this threat in the
        future. Only allowlisted projects can use this method during
        Early Access. Please reach out to Sales or your customer
        engineer to obtain access.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import webrisk_v1

            async def sample_submit_uri():
                # Create a client
                client = webrisk_v1.WebRiskServiceAsyncClient()

                # Initialize request argument(s)
                submission = webrisk_v1.Submission()
                submission.uri = "uri_value"

                request = webrisk_v1.SubmitUriRequest(
                    parent="parent_value",
                    submission=submission,
                )

                # Make the request
                operation = client.submit_uri(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.webrisk_v1.types.SubmitUriRequest, dict]]):
                The request object. Request to send a potentially
                malicious URI to WebRisk.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.webrisk_v1.types.Submission` Wraps
                a URI that might be displaying malicious content.

        """
        # Create or coerce a protobuf request object.
        request = webrisk.SubmitUriRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.submit_uri,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            webrisk.Submission,
            metadata_type=webrisk.SubmitUriMetadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: Optional[operations_pb2.ListOperationsRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.ListOperationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.list_operations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[operations_pb2.GetOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.GetOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.get_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_operation(
        self,
        request: Optional[operations_pb2.DeleteOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a long-running operation.

        This method indicates that the client is no longer interested
        in the operation result. It does not cancel the operation.
        If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.DeleteOperationRequest`):
                The request object. Request message for
                `DeleteOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.DeleteOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.delete_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def cancel_operation(
        self,
        request: Optional[operations_pb2.CancelOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.CancelOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.cancel_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self) -> "WebRiskServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("WebRiskServiceAsyncClient",)
