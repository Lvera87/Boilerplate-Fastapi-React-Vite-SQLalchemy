import { useQuery } from '@tanstack/react-query';

import { fetchHealthStatus } from '@/api/health.js';

function HealthStatus() {
  const {
    data,
    isLoading,
    isError,
    error,
    refetch,
    isFetching,
  } = useQuery({
    queryKey: ['health'],
    queryFn: fetchHealthStatus,
  });

  if (isLoading) {
    return <p className="status status--info">Consultando estado del servidor…</p>;
  }

  if (isError) {
    return (
      <div className="status status--error">
        <p>Ocurrió un error al consultar el backend.</p>
        <pre>{error.message}</pre>
        <button type="button" onClick={() => refetch()} disabled={isFetching}>
          Reintentar
        </button>
      </div>
    );
  }

  return (
    <div className="status status--success">
      <p>Backend operativo ✅</p>
      <dl>
        <div className="status__row">
          <dt>Estado:</dt>
          <dd>{data.status}</dd>
        </div>
        <div className="status__row">
          <dt>Timestamp:</dt>
          <dd>{new Date(data.timestamp).toLocaleString()}</dd>
        </div>
      </dl>
      <button type="button" onClick={() => refetch()} disabled={isFetching}>
        Actualizar
      </button>
    </div>
  );
}

export default HealthStatus;
