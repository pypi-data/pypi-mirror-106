import typing

import System
import System.Reflection.Metadata


class MetadataUpdateHandlerAttribute(System.Attribute):
    """
    Specifies a type that should receive notifications of metadata updates.
    
    The  specified by this attribute must have at least one static method with the following signature:
    static void ClearCache(Type[]? updatedTypes)static void UpdateApplication(Type[]? updatedTypes)
    Once a metadata update is applied, ClearCache is invoked for every handler that specifies one. This gives update handlers
    an opportunity to clear any caches that are inferred based from the application's metadata. This is followed by invoking the UpdateHandler
    method is invoked letting applications update their contents, trigger a UI re-render etc. When specified, the updatedTypes
    parameter indicates the sequence of types that were affected by the metadata update.
    """

    @property
    def HandlerType(self) -> typing.Type:
        """Gets the type that handles metadata updates and that should be notified when any occur."""
        ...

    def __init__(self, handlerType: typing.Type) -> None:
        """
        Initializes the attribute.
        
        :param handlerType: A type that handles metadata updates and that should be notified when any occur.
        """
        ...


